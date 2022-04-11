import re
from string import whitespace


def refinder(pattern, script):
    if re.match(pattern, script):
        print("Match!", re.match(pattern, script).group())
    else:
        print("Not a Match!")


def refinder_all(pattern, script):
    if re.search(pattern, script):
        print("Search!", re.search(pattern, script).group())
    else:
        print("Not a Search!")


refinder(r'is', 'life is so cool')
refinder_all(r'is', 'life is so cool')

# 정규표현식

# \d 숫자와 매치, [0-9]와 같음
# \D 숫자가 아닌 것과 매치, ^[0-9]와 같음
# \s whitespace 문자와 매치, [\t\n\r\f\v]와 같음
# \S whitespace 문자가 아닌 것과 매치, [^\t\n\r\f\v]와 같음
# \w 문자 + 숫자와 문자와 매치, [a-zA-Z0-9_]와 같음
# \W 문자 + 숫자와 문자가 아닌 문자와 매치, [^a-zA-Z0-9_]와 같음
# \\ 메타 문자가 아닌 일반 문자 역슬래시(\)와 매치, 메타 문자 앞에 \를 붙이면 일반 문자를 의미
