import sys
N = int(sys.stdin.readline())
ans = (0, 10001)
for i in range(1, N + 1):
    J, M = map(int, sys.stdin.readline().split())
    R = (J - 1) % (1 + M)
    temp = ((J - R) // (M + 1) + 1) * 2
    if ans[1] > temp:
        ans = (i, temp)

print(ans[0], ans[1])