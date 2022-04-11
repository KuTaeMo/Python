import re

words = ['apple', 'cat', 'brave', 'darma', 'arise', 'blow', 'coat', 'above']

for i in words:
    m = re.match(r'a\D+', i)
    if m:
        # print(i)
        print(m.group())
