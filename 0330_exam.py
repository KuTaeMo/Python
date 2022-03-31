# 1
# from posixpath import split


# def chg(t):
#     chgt = t.split(':')

#     result = "#".join(chgt)
#     print(result)


# text = "a:b:c:d"

# chg(text)

# 2
# a = {'A': 90, 'B': 80}

# try:
#     print(a['C'])
# except:
#     print("70")

# 3
# a = [1, 2, 3]

# print(id(a))

# #a = a + [4, 5]

# a.extend([4, 5])

# print(id(a))
# +를 하고나면 주소값이 바뀌지만 extend를 하게 되면 주소값이 그대로 유지된다.

# 4
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

# for i in A:
#     if i >= 50:
#         print(i)

# 5
# a = int(input())

# n1 = 0
# n2 = 1
# n3 = n1 + n2
# num = [n1, n2]

# while n3 < a:
#     num.append(n3)
#     n1 = n2
#     n2 = n3
#     n3 = n1 + n2

# print(num)

# 6
# s = input()

# num = s.split(',')
# result = 0

# for n in num:
#     result = result + int(n)

# print(result)

# 7
# print("구구단을 출력할 숫자를 입력하세요(2~9):", end='')
# n = int(input())

# for i in range(9):
#     print(n*(i+1), end=' ')

# 8
# text = []
# with open("c:/Users/pcn04/Desktop/ktm/python/abc.txt", 'r') as f1:

#     for t in f1.readlines():
#         text.append(t)
#     print(text)

# text.reverse()

# result = ''.join(text)

# print("==== reverse ====")
# with open("c:/Users/pcn04/Desktop/ktm/python/abc.txt", 'w') as f2:
#     print(result)
#     f2.write(result)

# 9

# text = []
# result = 0
# with open("c:/Users/pcn04/Desktop/ktm/python/sample.txt", 'r') as f:
#     for readline in f.readlines():
#         text.append(int(readline.replace('\n', '')))


# for n in text:
#     result = result + n

# result = result / len(text)

# with open("c:/Users/pcn04/Desktop/ktm/python/sample.txt", 'a') as f2:
#     f2.write("평균 : " + str(result))

# 10
# class Calcurator:
#     def __init__(self, num):
#         self.num = num

#     def sum(self):
#         result = 0
#         for n in self.num:
#             result = result + n
#         return result

#     def avg(self):
#         result = sum(self.num) / len(self.num)
#         return result


# cal1 = Calcurator([1, 2, 3, 4, 5])
# print(cal1.sum())
# print(cal1.avg())

# cal2 = Calcurator([6, 7, 8, 9, 10])
# print(cal2.sum())
# print(cal2.avg())

# 11
# 1. PYTHONPATH 에 경로 추가히기
# 2. 해당 파일이 있는 경로로 이동하기

# 12

# 13
# def DashInsert(num):
#     number = list(map(int, num))
#     result = []
#     for i, n in enumerate(number):
#         result.append(str(n))
#         if i < len(number)-1:
#             is_odd = n % 2 == 1
#             is_next_odd = number[i+1] % 2 == 1

#             if is_odd and is_next_odd:
#                 result.append("-")
#             elif not is_odd and not is_next_odd:
#                 result.append("*")
#     return " ".join(result)


# a = input()

# print(DashInsert(a))

# 14
def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c != _c:
            _c = c
            if cnt:
                result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt += 1

    if cnt:
        result += str(cnt)
    return result


print(compress_string("aaabbcccccca"))
