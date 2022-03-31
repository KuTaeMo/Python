# f = open("D:\Python\새파일.txt", 'w')

# data = ""
# for i in range(1, 11):
#     data += "%d번째 줄입니다.\n" % i
# data += "===끝==="
# f.write(data)
# f.close()

# f = open("D:\Python\새파일.txt", 'r')
# while True:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

#     break

# f.close()

with open("D:\Python\새파일.txt", 'a') as f:
    f.write("추가합니다")
    f.write("추가합니다")
