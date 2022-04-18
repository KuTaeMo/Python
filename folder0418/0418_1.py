from scipy import stats
import os, re, sys
import pandas as pd
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pyModule import consoleClear

df2 = pd.read_csv('survey.csv')

male = df2.income[df2.sex == 'm']
female = df2.income[df2.sex == 'f']

ttest_result = stats.ttest_ind(male,female)

#print(ttest_result[1])

# Ttest_indResult(statistic=-0.10650308143428423, pvalue=0.9161940781163369)
# 0.9161940781163369

# pvalue 는 유의확률을 의미한다.
# 유의확률은 유의확률 값이 작을수록 유의한 차이가 있다고 해석할 수 있다.
# 일반적으로 95% 또는 99%를 유의한 확률의 기준으로 삼기 때문에 유의확률 값이 0.05 미만이거나 0.01 미만이면 유의한 차이가 나타난다고 할 수 있다.
# 여기서 유의확률(pvalue) 값은 0.916으로  1에 가까울 정도로 높다 따라서 남성과 여성의 수입 평균에 유의한 차이가 있다고 보기 어렵다.

corr = df2.corr(method='spearman')
#print(corr)

#print(df2.income.corr(df2.stress))

#corr.to_csv('corr.csv')

import statsmodels.formula.api as smf

model = smf.ols(formula = 'jobSatisfaction~English + stress + income', data=df2)
result = model.fit()

print(result.summary())
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:        jobSatisfaction   R-squared:                       0.187
# Model:                            OLS   Adj. R-squared:                  0.059
# Method:                 Least Squares   F-statistic:                     1.458
# Date:                Mon, 18 Apr 2022   Prob (F-statistic):              0.258
# Time:                        16:24:38   Log-Likelihood:                -35.038
# No. Observations:                  23   AIC:                             78.08
# Df Residuals:                      19   BIC:                             82.62
# Df Model:                           3
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept      4.9159      1.712      2.871      0.010       1.333       8.499
# English       -0.0064      0.003     -1.931      0.069      -0.013       0.001
# stress         0.2141      0.187      1.145      0.266      -0.177       0.606
# income         0.0004      0.000      1.125      0.275      -0.000       0.001
# ==============================================================================
# Omnibus:                        0.278   Durbin-Watson:                   0.989
# Prob(Omnibus):                  0.870   Jarque-Bera (JB):                0.457
# Skew:                          -0.036   Prob(JB):                        0.796
# Kurtosis:                       2.313   Cond. No.                     3.00e+04
# ==============================================================================

# Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
# [2] The condition number is large,  3e+04. This might indicate that there are
# strong multicollinearity or other numerical problems.