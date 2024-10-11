# HWsosnag.py
# 2024-09-27      /   writer: ksm

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

os.chdir('C:/Mtest/workpandas/data/0927금요일소상공인데이터')

font_name = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

path = '소상공인시장진흥공단_상가(상권)정보_서울_202112.csv'
df = pd.read_csv(path,encoding='UTF-8', index_col=False)
print(df.info())
cnt = df['상권업종대분류명'].value_counts()
# print(cnt)

'''
상권업종대분류명
음식            111654
소매            94320
생활서비스      58438
학문/교육       22765
부동산          14254
관광/여가/오락   7095
스포츠          4636
숙박            2132
'''

sosangx = df['상권업종대분류명'].value_counts().index
sosangy = df['상권업종대분류명'].value_counts()
socum = df['상권업종대분류명'].value_counts().cumsum()

plt.figure(figsize = (10,5))
sns.lineplot(x=sosangx,y=sosangy, c='g', marker = '^')
plt.title('상권업종 별 수')
plt.legend(sosangx, loc = 'upper right')
plt.show()

# middlex = df['상권업종중분류명'].value_counts().index
# middley = df['상권업종중분류명'].value_counts()

# print(middlex)
# plt.figure(figsize = (10,5))
# sns.lineplot(x=middlex,y=middley, c='g', marker = '^')
# plt.title('상권업종 별 수')
# plt.legend(sosangx, loc = 'upper right')
# plt.show()



















# 스타벅스 or 스타 벅스 or starbucks
# 이디야 or 이디아 or ediya Ediya
# 요거프레소 1층
# 위도 경도 값을 땡겨오기

# print(df[(df['상호명']=='스타벅스')|(df['상호명']=='스타 벅스')|(df['상호명']=='STARBUCKSCOFFEE')][['상호명','위도','경도']])
# '''
#          상호명         위도          경도
# 1544    스타벅스  37.582964  127.003887
# 2570    스타벅스  37.527147  126.874682
# 3608    스타벅스  37.523184  127.021629
# 3687    스타벅스  37.535134  126.899952
# 4684    스타벅스  37.517450  126.896479
# ...      ...        ...         ...
# 279467  스타벅스  37.467265  127.099909
# 280359  스타벅스  37.562814  127.081329
# 280759  스타벅스  37.619249  127.079298
# 281361  스타벅스  37.554828  126.971712
# 281930  스타벅스  37.519593  127.034097

# [327 rows x 3 columns]
# '''
# print('- ' * 40) 