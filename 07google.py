import urllib.request
import requests
import os
import time

from PIL import Image
from io import BytesIO

url = 'http://www.google.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.90  Safari/537.36'}
r = requests.get(url, headers=headers)
print(r.text)

url = 'https://www.google.co.kr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
r2 = requests.get(url)
Image.open(BytesIO(r2.content))

print('이미지 이름', os.path.basename(url))

print('이미지파일명', os.getcwd())

name = os.path.basename(url)
path = os.path.join( image_folder, name)
my = open(path, 'wb')
my.write(r2.content)
my.close()