def is_odd(number):
    if(number % 2 == 1):
        return True
    else:
        return False


def avg_numbers(args):
    result = 0
    for i in args:
        result += i
    return result / len(args)


a = int(input())
if is_odd(a):
    print("홀수")
else:
    print("짝수")

print("다음")

d = []

print("입력하실 숫자의 개수를 입력하세요 : ")
cnt = int(input())

for i in range(cnt):
    print(i+1, "번째 숫자를 입력하세요 :")
    b = int(input())
    d.append(b)

print(d)

print(avg_numbers(d))
