import sys
N, m, M, T, R = map(int, sys.stdin.readline().split())
M -= m
if M < T:
    print(-1)
    exit()

cnt = 0
X = 0
while N:
    cnt += 1
    if X + T <= M:
        X += T
        N -= 1
    else:
        X -= R
        X = max(0, X)

print(cnt)