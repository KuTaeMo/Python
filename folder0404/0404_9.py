from asyncore import read
import csv
import os


def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output
    f.close()


os.chdir(r'C:\Users\pcn04\Desktop\ktm\python\csv')

print(opencsv('example2.csv'))
