import re

e = "Chandler: All right Joey, be nice. So does he have a dump? A hump and a hair-piece? Phoebe: wait, does he eat chalk? Phoebe: Jus, because, I don't wnt her to go throught what I went through with Carl- oh!"

m = re.findall(r'[A-Z|a-z]+:', e)
# print(m)

s = set(m)

l = list(s)

# cl = re.sub(':', '', l)

cl = []

for i in l:
    cl.append(re.sub(':', '', i))

print(cl)
