import time

print(time.time())
print(time.localtime(time.time()))
print(time.localtime(time.time()).tm_year, " 년", time.localtime(
    time.time()).tm_mon, " 월", time.localtime(time.time()).tm_mday, " 일 입니다.")
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print("=====================")
print(time.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.', time.localtime(time.time())))

# 출력결과
# 1648531946.142076
# time.struct_time(tm_year=2022, tm_mon=3, tm_mday=29, tm_hour=14,
#                  tm_min=32, tm_sec=26, tm_wday=1, tm_yday=88, tm_isdst=0)
# 2022  년 3  월 29  일 입니다.
# Tue Mar 29 14: 32: 26 2022
# Tue Mar 29 14: 32: 26 2022
# == == == == == == == == == == =
# 2022년 03월 29일 14시 32분 입니다.
