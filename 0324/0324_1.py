# 1번
국어 = 80
영어 = 75
수학 = 55

홍길동평균점수 = (국어+영어+수학)/3

# print(홍길동평균점수)

# 2번
a = 13
if a/2 == 0:
    b = "짝수"
else:
    b = "홀수"

# print(b)

# 3번
adNum = "881120-1068234"
yyyymmdd = adNum[:6]
num = adNum[7:]

#print(yyyymmdd, "-", num)

# 4번
adNum = "881120-1068234"
if adNum[7] == "1":
    s = "남자"
else:
    s = "여자"

# print(s)

# 5번
a = "a:b:c:d"
b = a.replace(":", "#")

# print(b)

# 6번
l1 = [1, 3, 5, 4, 2]
l1.sort()
l1.reverse()

# print(l1)

# 7번
l2 = ['life', 'is', 'too', 'short']
result = " ".join(l2)

# print(result)

# 8번
t1 = (1, 2, 3)
t1 = t1 + (4,)

# print(t1)

# 9번
d1 = dict()
# print(d1)
d1['name'] = 'python'
d1[250] = 'python'
# d1[[1]] = 'python' -> 리스트는 딕셔너리 자료형의 키값이 될 수 없다.
d1[('a',)] = 'python'
# print(d1)

# 10번
d2 = {'a': 90, 'b': 80, 'c': 70}
result = d2.pop('b')
# print(result)

# 11번
l3 = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
l3s = set(l3)
l3 = list(l3s)
# print(l3)

# 12번
x = y = [1, 2, 3]
x[1] = 4
# print(y)
