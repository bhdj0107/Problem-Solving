# 2020 07 02 1911 start
import sys
N, M = map(int, sys.stdin.readline().split())
cnt = [0 for _ in range(M)]
inp = list(map(int, sys.stdin.readline().split()))
for i in inp:
    cnt[i - 1] += 1
print(max(cnt))