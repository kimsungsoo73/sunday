import requests
import urllib.request
import json
import xmltodict

serviceKey = 'tGWp1FmEm4/LIWPvVf90Y5pR2Ol2GT0rvBbmrmgL/1vA+WfuuNblqNW3pekdv4pLfT1gqL33eQ+tGp4tZtnS4g=='
url = 'http://apis.data.go.kr/B553530/TRANSPORTATION/ELECTRIC_CHARGING'
params = {'serviceKey':serviceKey, 'pageNo':'1', 'numOfRows':'10', 'apiType':'xml', 'q1':'울산광역시', 'q2':'중구'}

response = requests.get(url, params = params)
print(response.content)

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

def getProject(pageNo, numOfRows, apiType, q1, q2):
    serviceKey = 'tGWp1FmEm4/LIWPvVf90Y5pR2Ol2GT0rvBbmrmgL/1vA+WfuuNblqNW3pekdv4pLfT1gqL33eQ+tGp4tZtnS4g=='
    url = 'http://apis.data.go.kr/B553530/TRANSPORTATION/ELECTRIC_CHARGING'
    parameter = '?_type=json&serviceKey='+serviceKey
    parameter = parameter + '&pageNo=' + str(pageNo) + '&numOfRows=' + str(numOfRows)
    parameter = parameter + '&apiType=' + apiType + '&q1=' + urllib.parse.quote(q1) + '&q2=' + urllib.parse.quote(q2)
    url = url + parameter 
    print(url)
    print('-'*70)
    ret_data = getRequestURL(url)

    if ret_data == None:
        None
    else:
        json_data = json.dumps(xmltodict.parse(ret_data), indent = 4)
        json_data = json.loads(json_data)
    return json_data

result = []
pageNo = 1
numOfRows = 10
    # print('|{:0>10,}'.format(1234))
json_data= getProject(pageNo,numOfRows,"xml","서울","마포구")
for i in range(numOfRows):
    if(json_data["response"]["header"]["resultMsg"] == "NORMAL_CODE"):
        RGN_MST = json_data["response"]["body"]["items"]['item'][i]["RGN_MST"]
        RGN_SUB = json_data["response"]["body"]["items"]['item'][i]["RGN_SUB"]
        ITEM_6 = json_data["response"]["body"]["items"]['item'][i]["ITEM_6"]
        DATA_REG_DT = json_data["response"]["body"]["items"]['item'][i]["DATA_REG_DT"]
        print(f'{RGN_MST} {RGN_SUB} {ITEM_6} {DATA_REG_DT}')
        result.append([RGN_MST]+[RGN_SUB]+[ITEM_6]+[DATA_REG_DT])

import pandas as pd

print(result)
df = pd.DataFrame(result)
path = './data.xml.csv'
df.to_csv(path, encoding = 'utf-8')
print(path, '파일 저장 성공')