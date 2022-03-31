import codecs

with codecs.open(r'C:\Users\pcn04\Desktop\ktm\python\새파일.txt', 'r', 'utf-8') as f:
    data = f.read()

print(data)
