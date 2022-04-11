import csv
import os

os.chdir(r'C:\Users\pcn04\Desktop\ktm\python\csv')
f = open('a.csv', 'r')

new = csv.reader(f)
a_list = []
for i in new:
    print(i)
    a_list.append(i)

print(a_list)
