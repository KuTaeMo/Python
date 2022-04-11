with open("D:/Python/새파일.txt", 'w') as f:
    data = ""
    for i in range(10):
        data += "%d 번째 입력입니다.\n" % (i+1)
    f.write(data)

with open("D:/Python/새파일.txt", 'r') as f1:
    for line in f1.readlines():
        print(line)
