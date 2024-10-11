import pandas as pd
import numpy as np
import time
import os
import folium
os.chdir('C:/Mtest/workpandas/data/0927금요일소상공인데이터')

df = pd.read_csv('소상공인시장진흥공단_상가(상권)정보_서울_202112.csv', encoding='utf-8')

time.sleep(2)
star = df[df['상호명'].str.contains('스타벅스|스타 벅스|starbucks', na=False)]
address = star.지번주소


addresslist = address.values.tolist()
locations = star[['위도', '경도']]
locationlist = locations.values.tolist()
len(locationlist)
# locationlist[7]

map = folium.Map(location=[37.5174497816404,126.89647871302], zoom_start=12)
for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point],
                 tooltip="Click me!",
                 popup = addresslist[point],
                 icon = folium.Icon(
                     color = 'blue',
                     icon_color = 'brown',
                     icon = 'coffee'
                 )).add_to(map)
map
path = 'test1.html'
map.save(path)