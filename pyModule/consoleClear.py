import os

def clear():
    command = 'clear'
    # nt 윈도우
    # posix 우분투 등의 리눅스
    # dos 는 모르겠음 
    if os.name in ('nt','dos'):
        command = 'cls'
    os.system(command)