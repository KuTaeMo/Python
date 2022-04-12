import os, re, sys
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from folder0404 import usecsv

os.chdir(r'C:\Users\pcn04\Desktop\ktm\doit 실습파일\05')

quest = np.array(usecsv.switch(usecsv.opencsv('quest.csv')))

quest[quest>5]=5

print(quest)

os.chdir(r'C:\Users\pcn04\Desktop\ktm\python')

usecsv.writecsv('resultcsv.csv',list(quest))
