with open("D:\Python\새파일1t.txt", 'a') as f:
    f.write("java is a good language\n")

with open("D:\Python\새파일1t.txt", 'r') as f1:
    body = f1.read()

body = body.replace("java", "python")

with open("D:\Python\새파일1t.txt", 'a') as f2:
    f2.write(body)
