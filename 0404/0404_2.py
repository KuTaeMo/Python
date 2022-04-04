import codecs
import re

lines = []

with codecs.open("take.txt", 'r', 'utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    p = re.compile('take')
    lines[i] = p.sub('테이크', line)
    print(p.sub('테이크', line))

print(lines)
