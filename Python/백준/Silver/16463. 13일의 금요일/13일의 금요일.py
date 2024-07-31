import sys
N = int(sys.stdin.readline())

class Date:
    def __init__(self):
        self.year = 2019
        self.month = 1
        self.day = 4
        self.monthTable = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    def isYoon(self):
        fourh = self.year % 400 == 0
        h = self.year % 100 == 0
        f = self.year % 4 == 0
        if fourh: return True
        if not fourh and h: return False
        if not h and f: return True
        return False

    def addOneWeek(self):
        self.day += 7
        if self.month == 2:
            if self.isYoon():
                monthEnd = 29
            else:
                monthEnd = 28
        else:
            monthEnd = self.monthTable[self.month - 1]
        
        if self.day > monthEnd:
            self.day -= monthEnd
            self.month += 1
            if self.month > 12:
                self.year += 1
                self.month = 1

start = Date()
cnt = 0
while True:
    if start.day == 13: cnt += 1
    start.addOneWeek()
    if start.year == N + 1: break
print(cnt)