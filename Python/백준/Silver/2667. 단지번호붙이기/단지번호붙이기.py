import sys
from collections import deque

N = int(sys.stdin.readline())
field = [sys.stdin.readline().rstrip() for _ in range(N)]

visited = [[0 for _ in range(N)] for _ in range(N)]

cnt = 0
cnts = []

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

for i in range(N):
    for j in range(N):
        if field[i][j] == '1' and visited[i][j] == 0:
            cnt += 1
            q = deque()
            q.append((i, j))
            tmpCnt = 0
            while q:
                y, x = q.popleft()
                if visited[y][x] == 1: continue
                else:
                    visited[y][x] = 1
                    tmpCnt += 1
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if ny >= 0 and ny < N and nx >= 0 and nx < N:
                            if field[ny][nx] == '1':
                                q.append((ny, nx))
            cnts.append(tmpCnt)
print(cnt)
cnts.sort()
[print(cnts[i]) for i in range(cnt)]