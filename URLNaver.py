# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json
import pandas as pd

data = input('단어 입력 >> ')
encText = urllib.parse.quote(data)

client_id = "A8i3mcaGmcNAs8Re08e2"
client_secret = "von4FGXasv"
encText = urllib.parse.quote("검색할 단어")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

print()
print('10-07-monday 제주 블로그 검색')

df = pd.DataFrame()
item = json.loads(response_body)['items']
title = []
description = []
for k in range(10):
    title.append(item[k]['title'])
    description.append(item[k]['description'])




