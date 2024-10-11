import os
import urllib.request
import json

url = 'https://api.github.com/repositories'
savename = "./data/my1002.json"
if not os.path.exists(savename):
    urllib.request.urlretrieve(url, savename)

print(savename)

items = json.load(open(savename, "r", encoding = 'utf-8'))

path = open(savename, "r", encoding='utf-8').read()
mydata = json.loads(path)

for item in mydata:
    print(item["name"]+":"+item["owner"]['login'])