# 2021 09 28 2200 start
import sys
def a():
    N, M = map(int, sys.stdin.readline().split())
    data = {}
    for _ in range(N):
        t = sys.stdin.readline().rstrip()
        if t in data: data[t] += 1
        else: data[t] = 1
    K = int(sys.stdin.readline())

    ans = 0
    for i in data:
        zero = i.count('0')
        if zero % 2 == K % 2 and zero <= K: ans = max(ans, data[i])
    print(ans)
a()
