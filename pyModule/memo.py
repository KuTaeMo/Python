import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    with open('memo.txt', 'r') as f:
        for line in f.readlines():
            print(line)
elif option == '-u':
    with open('memo.txt', 'r') as f:
        for line in f.readlines():
            print(line.upper())
