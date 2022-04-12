import os, re, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from folder0404 import usecsv
from pyModule import consoleClear

total = usecsv.opencsv('popSeoul.csv')

newPop = usecsv.switch(total)

consoleClear.clear()

new = [['구','한국인','외국인','외국인 비율(%)']]

for i in newPop:
    try:
        foreign = round(i[2]/(i[1]+i[2])*100,1)
        new.append([i[0],i[1],i[2],foreign])
    except:
        pass

for i in new:
    try:
        if(i[3]>3):
            print(i)
    except:
        pass

usecsv.writecsv('newPop.csv',new)