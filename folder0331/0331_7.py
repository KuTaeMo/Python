import codecs
import os
import re

with codecs.open('friends101.txt', 'r', 'utf-8') as f:
    script101 = f.read()

monicaScripts = re.findall(r'Monica:.+', script101)

# print(monicaScripts[:3])

for i in monicaScripts[:3]:
    print(i)

monica = ''

for j in monicaScripts:
    monica += j+'\n'

with codecs.open('monica.txt', 'w', 'utf-8') as f1:
    f1.write(monica)
