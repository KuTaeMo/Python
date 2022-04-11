import re

example1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년입니다.'

# 탐욕스럽다 (greedy)
print(re.findall(r'\d.+년', example1))
# 탐욕제어하기 (?)
print(re.findall(r'\d.+?년', example1))
print(re.findall(r'\d+년', example1))
print(re.findall(r'\d.년', example1))
