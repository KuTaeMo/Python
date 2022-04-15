import pandas as pd, os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pyModule import consoleClear

data = {'name':['Mark','Jane','Chris','Ryan'],'age':[33,32,44,42],'score':[91.3,83.4,77.5,87.7]}

df = pd.DataFrame(data)

consoleClear.clear()

print(df)
##########
# result #
##########
#     name  age  score
# 0   Mark   33   91.3
# 1   Jane   32   83.4
# 2  Chris   44   77.5
# 3   Ryan   42   87.7

print(df.sum())
##########
# result #
##########
# name     MarkJaneChrisRyan
# age                    151
# score                339.9
# dtype: object

print(df.age)
##########
# result #
##########
# Name: age, dtype: int64