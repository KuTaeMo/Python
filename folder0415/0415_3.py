import os, re, sys
import pandas as pd
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pyModule import consoleClear

df2 = pd.read_csv('survey.csv')

consoleClear.clear()

#print(df2.head())

#print(df2[:10].sort_values(by='jobSatisfaction',ascending=False))

#print(df2.mean())

# 평균 구하기
#print(df2.income.mean())

# 합 구하기
#print(df2.income.sum())

# 중앙값 구하기
#print(df2.income.median())

# 데이터프레임 기초통계량
#print(df2.describe())

# 데이터프레임 중 수입의 기초통계량
#print(df2.income.describe())

# 데이터프레임 빈도 분석하기
#print(df2.sex.value_counts())

print(df2.groupby(df2.sex).mean())