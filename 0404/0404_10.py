import csv

a = [['구', '전체', '내국인', '외국인'], ['관악구', '1', '2', '3'], [
    '강남구', '1', '2', '3'], ['송파구', '1', '2', '3'], ['강동구', '1', '2', '3']]

f = open('abc.csv', 'w',  newline='')

csvobject = csv.writer(f, delimiter=',')

csvobject.writerows(a)
f.close()
