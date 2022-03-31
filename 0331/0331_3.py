import re


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
