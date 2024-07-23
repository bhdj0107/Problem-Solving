import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
field = [sys.stdin.readline().rstrip() for _ in range(N)]

q = deque()
q.append(((0, 0), (0, 0)))
dist = [[0 for _ in range(M)] for _ in range(N)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

while q:
    prev, now = q.popleft()
    if dist[now[0]][now[1]] != 0: continue
    else:
        dist[now[0]][now[1]] = dist[prev[0]][prev[1]] + 1
        for k in range(4):
            ny = now[0] + dy[k]
            nx = now[1] + dx[k]
            if ny >= 0 and ny < N and nx >= 0 and nx < M:
                if field[ny][nx] == '1':
                    q.append((now, (ny, nx)))
print(dist[N - 1][M - 1])