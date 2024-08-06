import sys
from collections import deque

N = int(sys.stdin.readline())
field = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

def isSameColor(c1, c2, rgDisorder):
    if rgDisorder: colorMap = {'R':0, 'G':0, 'B':1}
    else: colorMap = {'R':2, 'G':0, 'B':1}

    c1 = colorMap[c1]
    c2 = colorMap[c2]
    return c1 == c2


nonRG = 0
visited = [[False for _ in range(N)] for _ in range(N)]

dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)

for i in range(N):
    for j in range(N):
        if visited[i][j]: continue
        else:
            nonRG += 1
            startColor = field[i][j]
            q = deque()
            q.append((i, j))
            while q:
                y, x = q.popleft()
                if visited[y][x]: continue
                else:
                    visited[y][x] = True
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
                        else:
                            if isSameColor(startColor, field[ny][nx], False): q.append((ny, nx))

RG = 0
visited = [[False for _ in range(N)] for _ in range(N)]

dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)

for i in range(N):
    for j in range(N):
        if visited[i][j]: continue
        else:
            RG += 1
            startColor = field[i][j]
            q = deque()
            q.append((i, j))
            while q:
                y, x = q.popleft()
                if visited[y][x]: continue
                else:
                    visited[y][x] = True
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
                        else:
                            if isSameColor(startColor, field[ny][nx], True): q.append((ny, nx))

print(nonRG, RG)