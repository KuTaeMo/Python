class MyError(Exception):
    def __str__(self) -> str:
        return "허용되지 않는 닉네임입니다."


def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print("입력한 닉네임 : ", nick)


try:
    print("닉네임을 입력하세요 : ", end='')
    nick = input()
    say_nick(nick)
except MyError as e:
    print(e)
