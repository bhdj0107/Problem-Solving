import sys
import datetime
input = sys.stdin.readline
week = ('MON','TUE','WED','THU','FRI','SAT','SUN')
m, d = map(int, input().split())
print(week[datetime.datetime(2007,m,d).weekday()])