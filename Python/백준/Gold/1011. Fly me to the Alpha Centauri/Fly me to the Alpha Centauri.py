# 2021 09 13 2206 start
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    d = y - x
    for i in range(1, 50000):
        a = (i - 1) * i
        b = i * (i + 1)
        if a < d and d <= b:
            total = i * 2
            break
    if d - (a + 1) > b - d:
        print(total)
    else:
        print(total - 1)