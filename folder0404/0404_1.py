import codecs
import re

with codecs.open('friends101.txt', 'r', 'utf-8') as f:
    script101List = f.readlines()

lines = []

for readline in script101List:
    if re.match(r'[A-Z][a-z]+:', readline):
        lines.append(readline)

would = [i for i in script101List if re.match(
    r'[A-Z][a-z]+:', i) and re.search('would', i)]

with codecs.open("would.txt", 'w', 'utf-8') as f1:
    f1.writelines(would)

print(would)

take = [i for i in script101List if re.match(
    r'[A-Z][a-z]+:', i) and re.search('take', i)]

with codecs.open("take.txt", 'w', 'utf-8') as f1:
    f1.writelines(take)

print(take)
