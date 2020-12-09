import pandas as pd
import requests
from urllib.parse import urlparse, parse_qsl, urlencode


api_key = "AIzaSyALk03GGX95h8w7rRoCuJXYjKkzxIqzVXg"  # 要去申請金鑰

'''
=== Notes ===
  - 研究每個金鑰可以抓幾筆資料
  - 研究 sharing key
  - 可能可以寫個 if-else + list + while/for loop，每當存取上限到了之後就換另一把金鑰
'''

# STEP 1. Get location place id around the assigned coord (API 1)

base_end_point = "" # an URL  # remove data type (between / and ?) and defult parameters (after ?, depart by &)  # sample in GMP document
data_type = ""  # json or xml
params = {}  # parameters to access APIs  # data type =  dictionary  # details in GMP document
params_encoded = urlencode(params)  # change the parameters into the API-requested format
end_point = f"{base_end_point}{data_type}?{params_encoded}"
requests.get(end_point).json()  # get the API data and change into json
# --- start to parse the content and find all place ids --- #
place_ids = []  # save the place_id into a list

'''
=== Notes ===
  - Important optional parameters: language, circle, place_id
  - Def an function
  - Need a correct coordinate, 只能看方圓
  - Save place ids in to a list
  - 研究 API parameters
  - 要找一組 coordinate 做為台大周遭每區的搜尋中心點
'''

# STEP 2. Use place ids to get detailed imformation of places (API 2)

for id in place_ids:
    {
        # API function
        # place_id changing
    }
# --- start to parse the content and find details --- #

# STEP 3. Make a Google API Client <-- Maybe can use the code from Google

'''
=== Notes ===
  - Same structure to Step 1, maybe can share the function
  - 研究 API parameters
  - 好像有寫好的可以直接用("https://github.com/googlemaps/google-maps-services-python") <-- 待研究
'''

'''
reference: "https://www.youtube.com/watch?v=ckPEY2KppHc" (45:00以前)
'''