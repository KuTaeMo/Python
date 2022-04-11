import codecs
import re

with codecs.open('friends101.txt', 'r', 'utf-8') as f:
    script101 = f.read()

char = re.compile(r'[A-Z][a-z]+:')

# print(re.findall(char, script101))

charList = re.findall(char, script101)

# print(set(charList))

z = list(set(charList))

character = []
for i in z:
    character += [i[:-1]]

print(character)
