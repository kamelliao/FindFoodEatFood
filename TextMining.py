from ckiptagger import data_utils, construct_dictionary, WS
import pandas as pd
import numpy as np
from PIL import Image
from wordcloud import WordCloud

class Review:
    def __init__(self, review_file_path, opinion_word_file_path, stop_word_file_path, mask_file_path, font_file_path, ws_data_file_path):
        self._mask_file_path = str(mask_file_path)
        self._font_file_path = str(font_file_path)
        self._review_file_path = str(review_file_path)
        self._opinion_word_file_path = str(opinion_word_file_path)
        self._stop_word_file_path = str(stop_word_file_path)
        self._ws_data_file_path = str(ws_data_file_path)
        self._review_df = self.review_csv2df()
        self._review_dict = self.review_csv2dict()
        self._opinion_word_df = self.opinion_csv2df()
        self._store_review = self.store_review_score()  # [[ids, store_name, score], ...]
        self._stop_word_list = self.stop_word_list()  # stop word list
        # review_file_path：店家評論的 csv 檔，colname = [general_type, specific_type, place_id, name, review1, review2, review3, review4, review5, IG_comment, IG_link]
        # opinion_word_file_path：算分用的 csv 檔，colname = [Word, Score]
        # stop_word_file_path：移除 stopword 用的 txt 檔，可以自由增減
        # mask_file_path：用來畫文字雲外框的 png 檔
        # font_file_path：用來畫文字雲的字型 otf 檔
        # ws_data_file_path：用來 training 如何斷句的資料檔

    @property
    def review_df(self):
        return self._review_df

    @property
    def review_dict(self):
        return self._review_dict

    @property
    def opinion_word_df(self):
        return self._opinion_word_df

    @property
    def store_review(self):
        return self._store_review

    @property
    def stop_words(self):
        return self._stop_word_list

    # opinion_csv2df：讀入 opinion word csv檔，轉變成 dataframe
    def opinion_csv2df(self):
        df = pd.read_csv(self._opinion_word_file_path, encoding = "big5")
        print("opinion_csv2df done")
        return df

    # review_csv2df：讀入 all_review csv檔，轉變成 dataframe
    def review_csv2df(self):
        df = pd.read_csv(self._review_file_path, encoding = "utf-8")
        print("review_csv2df done")
        return df

    # review_csv2dict：讀入 csv 檔，轉變成 Dictionary 
    def review_csv2dict(self):
        df = pd.read_csv(self._review_file_path, encoding = "utf-8")
        ids = df["place_id"].to_list()
        place_name = df["name"].to_list()
        cate = df["general_type"].to_list()
        sub_cate = df["specific_type"].to_list()
        comment1 = df["review1"].to_list()
        comment2 = df["review2"].to_list()
        comment3 = df["review3"].to_list()
        comment4 = df["review4"].to_list()
        comment5 = df["review5"].to_list()
        IG_comment = df["IG_comment"].to_list()
        ig_link = df["IG_link"].to_list()
        region = df["region"].to_list()
        review_dict = {}
        for i in range(len(ids)):
            review_dict[ids[i]] = {
                "name": place_name[i],
                "review": [str(comment1[i]), str(comment2[i]), str(comment3[i]), str(comment4[i]), str(comment5[i]), str(IG_comment[i])],
                "general_type": cate[i],
                "specific_type": sub_cate[i],
                "ig_link": ig_link[i],
                "region": region[i]
            }
        print("review_csv2dict done")
        return review_dict

    # stop_word_list：讀入 stopword.txt
    def stop_word_list(self):
        f = open(file = self._stop_word_file_path, mode = "r")
        stop_words = f.readlines()
        for i in range(len(stop_words)):
            stop_words[i] = stop_words[i].strip("\n")
        f.close()
        print("stop_word_list done")
        return stop_words

    # store_review_score：算每家店的評價分數
    def store_review_score(self):
        opinion_words = self._opinion_word_df["Word"].to_list()
        word_score = self._opinion_word_df["Score"].to_list()
        store_review = []
        ws = WS(self._ws_data_file_path)

        for ids in self._review_dict.keys():
            # CKIP  # 斷句
            word_list = ws(
                    self._review_dict[ids]["review"],
                    sentence_segmentation = True, # To consider delimiters
                    segment_delimiter_set = {"，", "。", "：", "？", "！", "；"}
                    )

            all_word_list = []  # 每家店的 tokens
            score = 0  # 每家店的評價分數
            # wordlist: [[tokens of review 1], [tokens of review 1], ...]
            for sentence in word_list:
                for i in range(len(sentence)):
                    if sentence[i] in opinion_words:
                        row = opinion_words.index(sentence[i])  # 找到 Opinion word 的位置
                        if i == 0:
                            score += float(word_score[row])
                            all_word_list += [sentence[i]]
                        elif sentence[i-1] == "不":  # 看看受不受否定詞影響
                            score += -1 * float(word_score[row])
                            all_word_list += ["不" + sentence[i]]
                        else:
                            score += float(word_score[row])
                            all_word_list += [sentence[i]]
                    else:
                        continue

            score_stdz = score / (len(all_word_list) + 1) * 10  # 除上 token 數，標準化成 score per token of this store
            
            store_review.append([ids, self._review_dict[ids]["name"], score_stdz])

            print("Counting score...")

        del ws
        print("store_review_score done")
        return store_review

    # wordcloud：畫每家店的文字雲
    def wordcloud(self):
        ws = WS(self._ws_data_file_path)
        puncs = ["，", "。", "：", "？", "！", "；", "「", "」", ".", "?", "!", ";", "...", "..", "~", "～", "(", ")", "（", "）", ">", "<", "$"]

        for ids in self._review_dict.keys():
            all_word_list_unclean = []
            all_word_list_clean = []
            word_list = ws(
                    self._review_dict[ids]["review"],
                    sentence_segmentation = True,  # To consider delimiters
                    segment_delimiter_set = {"，", "。", "：", "？", "！", "；"})

            for sentence in word_list:
                # 合併五條評論、處理「不」的問題
                for i in range(len(sentence)):
                    if i == 0:
                        all_word_list_unclean += [sentence[i]]
                    else:
                        if sentence[i-1] == "不":
                            all_word_list_unclean += [("不" + sentence[i])]
                        else:
                            all_word_list_unclean += [sentence[i]]
                
                # 去除標點符號、去除無意義字  
                all_word_list_clean += [word for word in all_word_list_unclean\
                    if word not in puncs and word not in self._stop_word_list]

            # 文字雲
            # .py檔的資料夾中須包含一個叫 "WordCloud" 的資料夾
            # "WordCloud" 裡要有叫 "cloud.png" 的 png 圖檔作為文字雲輪廓。還需要字型檔 (.otf)
            store_name = self._review_dict[ids]["name"]
            storage_path = f"./WordCloud/{store_name}.png"
            mask = np.array(Image.open(self._mask_file_path))
            wc = WordCloud(
                font_path = self._font_file_path,
                background_color = "white",
                max_words = 200,
                mask = mask
            )
            wc.generate(" ".join(all_word_list_clean))
            wc.to_file(storage_path)
            print("Making wordcloud....")
        del ws
        print("Making wordcloud done")
        return

# all review
while True:
    review_file_path = "https://github.com/chhtwhc/FindFoodEatFood/raw/main/crawling/all_review.csv"
    opinion_word_file_path = "./CSentiPackage/ANTUSD_traditional/opinion_word.csv"  # 固定的
    stop_word_file_path = "./stop_words.txt"  # 固定的
    mask_file_path = "./WordCloud/cloud.png"  # <<< 語晰可能會給新的 .png 檔，現在是固定的
    font_file_path = "./WordCloud/NotoSansCJKtc-hinted/NotoSansCJKtc-Regular.otf"  # <<< 語晰可能會給新的 .otf檔，現在是固定的
    ws_data_file_path = "./data"  # 固定的
    review_all = Review(
                    review_file_path = review_file_path,
                    opinion_word_file_path = opinion_word_file_path,
                    stop_word_file_path = stop_word_file_path,
                    mask_file_path = mask_file_path,
                    font_file_path = font_file_path,
                    ws_data_file_path = ws_data_file_path)

    review_all.wordcloud()
    print(review_all.store_review_score, end = "\n==========\n")

    break

# output a csv (all in one)
while True:
    # merge store id
    all_store_id = review_all.review_dict.keys()

    # merge store region
    all_store_region = []
    for ids in review_all.review_dict.keys():
        all_store_region.append(review_all.review_dict[ids]["region"])    
    
    # merge store name
    all_store_name = []
    for i in range(len(review_all.store_review)):
        all_store_name.append(review_all.store_review[i][1])

    # merge store score and standardize
    all_store_score = []
    all_store_score_stdz = []
    for i in range(len(review_all.store_review)):
        all_store_score.append(review_all.store_review[i][2])

    score_max = max(all_store_score)
    for score in all_store_score:
        all_store_score_stdz.append((score / score_max) * 10)  # standardize to 1~10 分

    # merge store general type
    all_store_general_type = []
    for ids in review_all.review_dict.keys():
        all_store_general_type.append(review_all.review_dict[ids]["general_type"])

    # merge store specific type
    all_store_specific_type = []
    for ids in review_all.review_dict.keys():
        all_store_specific_type.append(review_all.review_dict[ids]["specific_type"])

    # merge store IG_link
    all_store_IG_link = []
    for ids in review_all.review_dict.keys():
        all_store_IG_link.append(review_all.review_dict[ids]["ig_link"])

    # 匯出成 csv 檔
    all_dict = {
    "region": all_store_region,
    "Category": all_store_general_type,
    "Subcategory": all_store_specific_type,
    "Id": all_store_id,
    "Name": all_store_name,
    "Score": all_store_score_stdz,
    "IG_link": all_store_IG_link
    }  

    all_df = pd.DataFrame(all_dict)
    all_df = all_df.sort_values(by = ["Score"], ascending = False)  # 按照分數由高到低排
    all_df.to_csv("./TextMining.csv")

    break