import geopandas as gpd
import matplotlib.font_manager
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
def get_lat_lon(address):
    geolocator = Nominatim(user_agent="my_agent")
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except (GeocoderTimedOut, GeocoderServiceError):
        print("Error: 지오코딩 서비스에 문제가 발생했습니다. 다시 시도해주세요.")
        return None, None
# 주소 입력 받기 ~로 건물번호 형식 예) 서울 마포구 양화로 122
address = input("상세 주소를 입력하세요: ")
# 위도와 경도 얻기
lat, lon = get_lat_lon(address)
print(f"\n입력한 주소: {address}")
print(f"위도: {lat}")
print(f"경도: {lon}")

'''
http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList


(Encoding)	
tGWp1FmEm4%2FLIWPvVf90Y5pR2Ol2GT0rvBbmrmgL%2F1vA%2BWfuuNblqNW3pekdv4pLfT1gqL33eQ%2BtGp4tZtnS4g%3D%3D

http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList&stdt=20230101
tGWp1FmEm4%2FLIWPvVf90Y5pR2Ol2GT0rvBbmrmgL%2F1vA%2BWfuuNblqNW3pekdv4pLfT1gqL33eQ%2BtGp4tZtnS4g%3D%3D

<response>
	<header>
		<responseTime>2024-10-01T14:13:58.658+09:00</responseTime>
		<resultCode>30</resultCode>
		<resultMsg>SERVICE KEY IS NOT REGISTERED ERROR.</resultMsg>
	</header>
</response>
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
import seaborn as sns
import urllib.request
import json

font_name = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False

# 1단계
def getRequestURL(url , encoding = 'utf-8'):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    if response.getcode() == 200:
        first = response.read()
        print(first)
        print('-'*50)

        ret = first.decode(encoding)
        print(ret)
    return ret

# 2단계
def getNatVisitor(returnType, yyyymm, nat_cd, ed_cd):
    serviceKey = '400iA9ln1XUUO3jxGMYEKx0ce9vcpw23Ag5htvt0M1Kjiefy%2F1sRLNBogr0aDAjMT9zZ1B9FEsmSbTv19x4r1w%3D%3D'
    url= 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    parameter = '?_type=json&serviceKey='+serviceKey
    parameter = parameter + '&returnType='+ returnType
    parameter = parameter + '&YM='+yyyymm
    parameter = parameter + '&NAT_CD='+nat_cd
    parameter = parameter + '&ED_CD='+ed_cd
    url = url + parameter
    print(url)
    print('-'*70)
    ret_data = getRequestURL(url)

    print(ret_data)
    return json.loads(ret_data)

# 3단계
result = []

for year in range(2020, 2023):
    for month in range(1,13):
        # print('|{:0>10,}'.format(1234))
        yyyymm = '{0}{1:0>2}'.format(str(year), str(month))
        json_data= getNatVisitor('json', yyyymm, '275', 'E')
        if(json_data['response']['header']['resultMsg'] == 'OK'):
            natKorNm = json_data['response']['body']['items']['item']['natKorNm']
            num = json_data['response']['body']['items']['item']['num']
            print('%s년 %s월 %s %s명' %(str(year),str(month), natKorNm, num))
            result.append([yyyymm] + [natKorNm] + ['275'] + [num] )

print(result)
df = pd.DataFrame(result)
path = './data.tour.csv'
df.to_csv(path, encoding = 'cp949')
print(path, '파일 저장 성공')

# restAPI접속 url 주소 및 ServiceKey 접속

# ymVisit = []
# cnVisit = []
# index = []
# i = 0

# for item in result:
#     ymVisit.append(item[0])
#     cnVisit.append(item[3])
#     index.append(i)
#     index += 1

# import os
# os.chdir('C:/Mtest/workRestapi')

# tour_csv = pd.read_csv('data.tour.csv', encoding = 'cp949')

# plt.figure(figsize = (10,7))
# plt.bar(ymVisit,cnVisit)
# plt.title('미국 출입국 통계데이터')
# plt.xlabel('방한년월')
# plt.ylabel('방문객 수')
# plt.show()