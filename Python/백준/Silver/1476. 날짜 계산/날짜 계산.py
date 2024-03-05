import sys
E, S, M = map(int, sys.stdin.readline().split())
E -= 1
S -= 1
M -= 1
# E 1 ~ 15, S 1 ~ 28, M 1 ~ 19
ans = 0
while True:
    if E == ans % 15 and S == ans % 28 and M == ans % 19:
        print(ans + 1)
        break
    else:
        ans += 1

