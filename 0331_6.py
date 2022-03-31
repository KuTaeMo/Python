import codecs
import re


sentence = 'I have a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog. SO WHAT? GOOD.'

#print(re.split(r'[.!?]', sentence))

data = 'a:3,b:4,c:5'

#print(re.split(r',', data))

# for i in re.split(r',', data):
#     print(re.split(r':', i))

#print(re.sub(r'dog', 'cat', sentence))

# with codecs.open(r'C:\Users\pcn04\Desktop\ktm\python\새파일.txt', 'r', 'utf-8') as f:
#     text = f.read()
#     print(text)
#     print("===================")
#     print(re.sub(r'\r\n', ' ', text))

print(re.findall(r'\w+ly', sentence))
