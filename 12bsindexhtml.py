from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np

filename = './data/index.html'
html = ''
with open(filename, 'r', encoding = 'utf-8') as file:
    for line in file:
        html += line

# print(html)

# 문제 1
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

#문제 2 <h2> ~~~ 내용 </h2> 태그 찾기

# print(soup.find_all('h2'))

# for data in soup.find_all('h2'):
#     print(data.text)

result= []
maintitle = []
subtitle_list = []
datelist = []

post_list = soup.find_all('div', {'class': 'post-preview'})

for data in post_list:
    title = data.find('h2', {'class':'post-title'}).text.strip()
    subtitle = data.find('h3', {'class':'post-subtitle'}).text.strip()
    date = data.find('p', {'class':'post-meta'}).text.strip()
    print(title ,'\t' , subtitle ,'\t', date )
    maintitle.append(title)
    subtitle_list.append(subtitle)
    datelist.append(date)

df = pd.DataFrame({'title':maintitle, 'subtitle': subtitle_list, 'date':datelist})
print(df)
for data in soup.find_all('p'):
    print(data.text)
