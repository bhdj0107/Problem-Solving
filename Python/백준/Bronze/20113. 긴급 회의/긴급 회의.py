import sys
N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
M = 0
ans = 0
cnt = 0
vote = [0 for _ in range(N + 1)]
for i in X:
    vote[i] += 1
for i in range(1, N + 1):
    if vote[i] > M:
        M = vote[i]
        ans = i
        cnt = 1
    elif vote[i] == M:
        cnt += 1
if cnt > 1:
    print('skipped')
else:
    print(ans)