# 載入套件
import pandas as pd
import numpy as np

# 讀取總資料集
all_info = pd.read_csv('all_info.csv', encoding='utf-8', converters={'periods': eval})

# 篩選資料並輸出前端要求的list
def filter_restaurants(all_info=all_info, info=info, date: int) -> list:
    list_result = []
    # 篩選食物與地區
    if info['Category']:
        # 當模式為「選餐廳」
        idx = np.where((all_info['region'].isin(info['region'])) & (all_info['Category'].isin(info['Category'])))
    else:
        # 當模式為「選食物」
        idx = np.where((all_info['region'].isin(info['region'])) & (all_info['Subcategory'] == info['Subcategory']))
    selected_restaurant = all_info.loc[idx]

    # 將篩選結果轉換成前端的輸出格式
    for _, row in selected_restaurant.iterrows():
        # 處理營業時間
        # 並不是每家店都0~6天都有
        time_week = row['periods']
        time_week_tbl = dict()
        if time_week is not None:
            for i, data_day in enumerate(time_week):
                time_week_tbl[data_day['close']['day']] = '{opent}-{closet}'.format(opent=data_day['open']['time'], closet=data_day['close']['time'])
            # 再判斷是否有該天的資料
            if date in time_week_tbl:
                time_day = time_week_tbl[date]
            else:
                time_day = 'None'
        else:
            time_day = 'None'

        # 將結果加入list
        date_map = {0: 'Sun', 1: 'Mon', 2: 'Tues', 3: 'Wed', 4: 'Thur', 5: 'Fri', 6: 'Sat'}  # 將輸入的日期轉為字串格式
        food_path = './food/{Id}.png'.format(Id=row['Id'])
        word_cloud_path = './wordcloud/{Id}.png'.format(Id=row['Id'])  # 文字雲檔案路徑
        busyness_path = './busyness/{Id}_{Date}.png'.format(Id=row['Id'], Date=date_map[date])  # 繁忙時間柱狀圖檔案路徑
        row_data = [row['Name'], row['Region'], row['pinyin'], row['Score'], row['Subcategory'], time_day, row['Google_link'], food_path, word_cloud_path, busyness_path]
        list_result.append(row_data)

    # 輸出結果
    return list_result

final_list = filter_restaurants(date=today)