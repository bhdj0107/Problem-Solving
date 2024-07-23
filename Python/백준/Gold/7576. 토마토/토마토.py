import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 0
q = deque()
dist = [[-1 for _ in range(M)] for _ in range(N)]

totalTomato = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == 1: q.append(((i, j), (i, j)))
        if field[i][j] != -1: totalTomato += 1
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
while q:
    prev, now = q.popleft()
    if dist[now[0]][now[1]] != -1: continue
    else:
        totalTomato -= 1
        dist[now[0]][now[1]] = dist[prev[0]][prev[1]] + 1
        for k in range(4):
            ny = now[0] + dy[k]
            nx = now[1] + dx[k]
            if ny >= 0 and ny < N and nx >= 0 and nx < M:
                if field[ny][nx] == 0:
                    q.append((now, (ny, nx)))

if totalTomato == 0: print(max(ans, max([max(i) for i in dist])))
else: print(-1)
