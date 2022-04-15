import os, re, sys, pandas as pd
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pyModule import consoleClear

#df = pd.read_csv('apt.csv',encoding='cp949')

consoleClear.clear()

#print(len(df))

#print(df.head())
#print(df.tail())
#print(df.지역)
#print(df.면적 >130)

#print(df[df.면적>130])
#print(df.가격[df.면적>130])
#print(df.가격[(df.가격<15000)&(df.면적>130)])
#print(df.loc[:,['아파트','가격']][df.가격 > 40000])

#df['단가'] = df.가격 / df.면적

#print(df.loc[:10,('가격','면적','단가')])

# print(df[df.가격>40000].sort_values(by='가격', ascending=False).loc[:,('가격','지역')])

# print(df.지역.str.find('강릉'))

#print(df[df.지역.str.find('강릉')>-1])

#dfF = df[df.지역.str.find('강릉')>-1]

#print(dfF.mean())

df = pd.read_csv('apt_comma.csv',encoding='cp949')


#print(df.가격>40000)

df.가격 = df.가격.str.replace(',','').astype('int64')

print(df[df.가격>40000])