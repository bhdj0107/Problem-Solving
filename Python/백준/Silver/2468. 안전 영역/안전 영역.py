import sys
sys.setrecursionlimit(10**8)
N = int(sys.stdin.readline())
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

num = set()
M = 1
inp = []
chk = [[False for _ in range(N)] for _ in range(N)]

for _ in range(N):
    temp = tuple(map(int, sys.stdin.readline().split()))
    num.update(temp)
    inp.append(temp)


def dfs(y, x):
    global chk
    if 0 <= x < N and 0 <= y < N:
        if chk[y][x]:
            chk[y][x] = False
            for i in range(4):
                dfs(y + dy[i], x + dx[i])


for D in num:
    cnt = 0
    chk = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if inp[i][j] > D:
                chk[i][j] = True
    for i in range(N):
        for j in range(N):
            if chk[i][j]:
                cnt += 1
                dfs(i, j)
    M = max(M, cnt)

print(M)