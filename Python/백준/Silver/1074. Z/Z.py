# 2021 09 27 2319 start
import sys
N, r, c = map(int, sys.stdin.readline().split())
r += 1
c += 1
cnt = 0
while True:
    if N == 0: break
    if r <= (2 ** N) // 2 and c <= (2 ** N) // 2:
        N -= 1
    elif r <= (2 ** N) // 2 and c > (2 ** N) // 2:
        cnt += (2 ** (N - 1)) * (2 ** (N - 1))
        c -= 2 ** (N - 1)
        N -= 1
    elif r > (2 ** N) // 2 and c <= (2 ** N) // 2:
        cnt += (2 ** (N - 1)) * (2 ** (N - 1)) * 2
        r -= 2 ** (N - 1)
        N -= 1
    elif r > (2 ** N) // 2 and c > (2 ** N) // 2:
        cnt += (2 ** (N - 1)) * (2 ** (N - 1)) * 3
        c -= 2 ** (N - 1)
        r -= 2 ** (N - 1)
        N -= 1
print(cnt)