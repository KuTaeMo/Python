import re, os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from folder0404 import usecsv
from pyModule import consoleClear

total = usecsv.opencsv('popSeoul.csv')

for i in total:
    for j in i:
        # if re.search('\d',j):
        #     k.append(float(re.sub(',','',j)))
        # else:
        #     k.append(j)
        # if re.search('[a-z가-힣]',j):
        #     k.append(j)
        # else:
        #     k.append(j)
        try:
            i[i.index(j)] = float(re.sub(',','',j))
        except:
            pass

consoleClear.clear()
print(total)  