import urllib.request
import requests
import json
from bs4 import BeautifulSoup # 사이트 주소 tag
from selenium import webdriver # 웹브라우저가동

import pandas as pd
import numpy as np
import time
import re

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

url = 'https://www.naver.com/'
request = urllib.request.urlopen(url)
response = request.read()
source = response.decode('utf-8')

soup = BeautifulSoup(source, 'html.parser')

driver = webdriver.Chrome()
driver.get(url)
data = driver.page_source

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.find_element(By.NAME, 'query').send_keys('파이썬' + Keys.ENTER)
soup = BeautifulSoup(source, 'html.parser')
print(soup)
time.sleep(10)