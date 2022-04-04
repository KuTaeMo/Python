import os
import usecsv

os.chdir(r'C:\Users\pcn04\Desktop\ktm\python\csv')

a = [['국어', '영어', '수학'], [90, 60, 100]]
usecsv.writecsv('test.csv', a)
