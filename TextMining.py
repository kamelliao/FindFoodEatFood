from ckiptagger import data_utils, construct_dictionary, WS
import pandas as pd
import numpy as np
from PIL import Image
from wordcloud import WordCloud

class Review:
    def __init__(self, review_file_path, opinion_word_file_path, stop_word_file_path, mask_file_path, font_file_path, ws_data_file_path, source = "google"):
        self._file_path = review_file_path
        self._review_df = self.csv2df(review_file_path)
        self._review_dict = self.csv2dict(review_file_path, source)
        self._opinion_word_df = self.csv2df(opinion_word_file_path)
        self._source = source
        self._store_review = self.store_review_score(source, ws_data_file_path)  # sorted list [[ids, store_name, score], ...]
        self._stop_word_list = self.stop_word_list(stop_word_file_path)  # stop word list
        self._mask_file_path = str(mask_file_path)
        self._font_file_path = str(font_file_path)

    @property
    def file_path(self):
        return self._file_path

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

    def csv2df(self, file_path):
        df = pd.read_csv(file_path, encoding = "big5")
        return df

    def csv2dict(self, file_path, source):
        df = pd.read_csv(file_path, encoding = "big5")
        if source == "google":
            ids = df["Place_id"].to_list()
            place_name = df["Place_name"].to_list()
            cate = df["Category"].to_list()
            sub_cate = df["Sub_Category"].to_list()
            comment1 = df["Comment1"].to_list()
            comment2 = df["Comment2"].to_list()
            comment3 = df["Comment3"].to_list()
            comment4 = df["Comment4"].to_list()
            comment5 = df["Comment5"].to_list()
            review_dict = {}
            for i in range(len(ids)):
                review_dict[ids[i]] = {
                    "store_name": place_name[i],
                    "comments": [str(comment1[i]), str(comment2[i]), str(comment3[i]), str(comment4[i]), str(comment5[i])],
                    "category": cate[i],
                    "sub_category": sub_cate[i]
                }
            return review_dict

        if source == "instagram":
            pass
            return review_dict
            # 等確定 ig review 的 csv 形式，做法和 csv2dict_google 一樣

        else:
            return "Wrong Source"

    def stop_word_list(self, file_path):
        f = open(file = file_path, mode = "r")
        stop_words = f.readlines()
        for i in range(len(stop_words)):
            stop_words[i] = stop_words[i].strip("\n")
        f.close()
        return stop_words

    def store_review_score(self, source, file_path):
        opinion_words = self._opinion_word_df["Word"].to_list()
        word_score = self._opinion_word_df["Score"].to_list()
        store_review = []
        ws = WS(file_path)

        if source == "google":
            for ids in self._review_dict.keys():
                sentence_list = self._review_dict[ids]["comments"]
                # CKIP  # 斷句
                all_word_list = []
                score = 0
                word_list = ws(
                        sentence_list,
                        sentence_segmentation = True, # To consider delimiters
                        segment_delimiter_set = {"，", "。", "：", "？", "！", "；"}
                        )

                for sentence in word_list:
                    for i in range(len(sentence)):
                        if sentence[i] in opinion_words:
                            row = opinion_words.index(sentence[i])
                            if i == 0:
                                score += float(word_score[row])
                            elif sentence[i-1] == "不":
                                score += -1 * float(word_score[row])
                            else:
                                score += float(word_score[row])
                            all_word_list += [sentence[i]]
                        else:
                            continue

                score_stdz = score / (len(all_word_list) + 1) * 10
                
                store_review.append([ids, self._review_dict[ids]["store_name"], score_stdz])

            del ws
            return store_review

        if source == "instagram":
            pass
            del ws
            return store_review
            # 等確定 ig review 的 csv 形式，做法和 google 一樣
        
        else:
            del ws
            return "Wrong Source"

    def wordcloud(self, source, file_path):
        ws = WS(file_path)
        puncs = ["，", "。", "：", "？", "！", "；", "「", "」", ".", "?", "!", ";", "...", "..", "~", "～", "(", ")", "（", "）", ">", "<", "$"]
        
        if source == "google":
            for ids in self._review_dict.keys():
                all_word_list_unclean = []
                all_word_list_clean = []
                word_list = ws(
                        self._review_dict[ids]["comments"],
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
                store_name = self._review_dict[ids]["store_name"]
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
                print("working....")
            del ws
            return


# google_118_review
review_file_path = "./FindFoodEatFood/crawling/118/118_google_reviews.csv"
opinion_word_file_path = "./CSentiPackage/ANTUSD_traditional/opinion_word.csv"
stop_word_file_path = "./stop_words.txt"
mask_file_path = "./WordCloud/cloud.png"
font_file_path = "./WordCloud/NotoSansCJKtc-hinted/NotoSansCJKtc-Regular.otf"
ws_data_file_path = "./data"
google_118_review = Review(
                review_file_path = review_file_path,
                opinion_word_file_path = opinion_word_file_path,
                stop_word_file_path = stop_word_file_path,
                mask_file_path = mask_file_path,
                font_file_path = font_file_path,
                ws_data_file_path = ws_data_file_path)

# google_118_review.wordcloud(source = "google", file_path = ws_data_file_path)
#print(google_118_review.store_review, end = "\n=====\n")
#print(google_118_review.review_dict)

'''
# google_wenzhou_review
review_file_path = "./FindFoodEatFood/crawling/wenzhou/wenzhou_google_reviews.csv"
opinion_word_file_path = "./CSentiPackage/ANTUSD_traditional/opinion_word.csv"
stop_word_file_path = "./stop_words.txt"
mask_file_path = "./WordCloud/cloud.png"
font_file_path = "./WordCloud/NotoSansCJKtc-hinted/NotoSansCJKtc-Regular.otf"
ws_data_file_path = "./data"
google_wenzhou_review = Review(
                review_file_path = review_file_path,
                opinion_word_file_path = opinion_word_file_path,
                stop_word_file_path = stop_word_file_path,
                mask_file_path = mask_file_path,
                font_file_path = font_file_path,
                ws_data_file_path = ws_data_file_path)

google_wenzhou_review.wordcloud(source = "google", file_path = ws_data_file_path)
print(google_wenzhou_review.store_review, end = "\n=====\n")

# google_gongguan_review
review_file_path = "./FindFoodEatFood/crawling/gongguan/gongguan_google_reviews.csv"
opinion_word_file_path = "./CSentiPackage/ANTUSD_traditional/opinion_word.csv"
stop_word_file_path = "./stop_words.txt"
mask_file_path = "./WordCloud/cloud.png"
font_file_path = "./WordCloud/NotoSansCJKtc-hinted/NotoSansCJKtc-Regular.otf"
ws_data_file_path = "./data"
google_gongguan_review = Review(
                review_file_path = review_file_path,
                opinion_word_file_path = opinion_word_file_path,
                stop_word_file_path = stop_word_file_path,
                mask_file_path = mask_file_path,
                font_file_path = font_file_path,
                ws_data_file_path = ws_data_file_path)

google_gongguan_review.wordcloud(source = "google", file_path = ws_data_file_path)
print(google_gongguan_review.store_review, end = "\n=====\n")
'''

# 匯出成CSV
all_store_id = google_118_review.review_dict.keys() # + google_wenzhou_review.review_dict.keys() + google_gongguan_review.review_dict.keys()
print("id = ", str(len(all_store_id)))
all_store_name = []
for i in range(len(google_118_review.store_review)):
    all_store_name.append(google_118_review.store_review[i][1])
'''
for i in range(len(google_wenzhou_review.store_review)):
    all_store_name.append(google_wenzhou_review.store_review[i][1])
for i in range(len(google_gongguan_review.store_review)):
    all_store_name.append(google_gongguan_review.store_review[i][1])
'''
print("name = ", str(len(all_store_name)))

all_store_score = []
all_store_score_stdz = []
for i in range(len(google_118_review.store_review)):
    all_store_score.append(google_118_review.store_review[i][2])
'''
for i in range(len(google_wenzhou_review.store_review)):
    all_store_score.append(google_wenzhou_review.store_review[i][2])
for i in range(len(google_gongguan_review.store_review)):
    all_store_score.append(google_gongguan_review.store_review[i][2])
'''

score_max = max(all_store_score)
for score in all_store_score:
    all_store_score_stdz.append((score / score_max) * 10)
print("score = ", str(len(all_store_score_stdz)))

all_store_category = []
for ids in google_118_review.review_dict.keys():
    all_store_category.append(google_118_review.review_dict[ids]["category"])
'''
for ids in google_wenzhou_review.review_dict.keys():
    all_store_category.append(google_wenzhou_review.review_dict[ids]["category"])
for ids in google_gongguan_review.review_dict.keys():
    all_store_category.append(google_gongguan_review.review_dict[ids]["category"])
'''
print("category = ", str(len(all_store_category)))

all_store_sub_category = []
for ids in google_118_review.review_dict.keys():
    all_store_sub_category.append(google_118_review.review_dict[ids]["sub_category"])
'''
for ids in google_wenzhou_review.review_dict.keys():
    all_store_category.append(google_wenzhou_review.review_dict[ids]["sub_category"])
for ids in google_gongguan_review.review_dict.keys():
    all_store_category.append(google_gongguan_review.review_dict[ids]["sub_category"])
'''
print("subcategory = ", str(len(all_store_sub_category)))

all_dict = {
    "Category": all_store_category,
    "Subcategory": all_store_sub_category,
    "Id": all_store_id,
    "Name": all_store_name,
    "Score": all_store_score_stdz
}


all_df = pd.DataFrame(all_dict)

all_df.to_csv("./TextMining.csv")


'''
待完成：
    1. __init__ 的問題
    2. 程式碼肥胖
    3. 匯出成 CSV
'''