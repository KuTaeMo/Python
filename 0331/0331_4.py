import re

number = 'My number is 511223-1****** and yours is 521012-2******'
print(re.findall('\d{6}', number))
print(re.findall('\d+\W{5}', number))

print("====================================")
print(re.findall(r'\d{6}[-]\d+\W{5}', number))
