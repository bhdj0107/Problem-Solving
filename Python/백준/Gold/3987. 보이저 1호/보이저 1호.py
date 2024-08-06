import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
field = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
R, C = map(lambda x:int(x) - 1, sys.stdin.readline().split())

q = deque()
# U, R, D, L
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
directionChanger = {'/': (1, 0, 3, 2),
                    '\\': (3, 2, 1, 0)}

maxStep = 1
maxDirection = 0
isLoop = False

for start in range(4):
    # (y, x, step, direction)
    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(4)]
    visited[start][R][C] = True
    q.append((R + directions[start][0], C + directions[start][1], 2, start))

    while q:
        y, x, numStep, directionIdx = q.popleft()
        if visited[directionIdx][y][x]:
            isLoop = True
            maxDirection = start
            break
        else:
            visited[directionIdx][y][x] = True
            if field[y][x] == 'C': continue
            if maxStep < numStep:
                maxStep = numStep
                maxDirection = start

            if field[y][x] in ('/', '\\'):
                newDirectionIdx = directionChanger[field[y][x]][directionIdx]
            elif field[y][x] == '.':
                newDirectionIdx = directionIdx

            ny = y + directions[newDirectionIdx][0]
            nx = x + directions[newDirectionIdx][1]
            if ny < 0 or ny >= N or nx < 0 or nx >= M: continue
            q.append((ny, nx, numStep + 1, newDirectionIdx))
    if isLoop: break

d2c = ['U', 'R', 'D', 'L']
print(d2c[maxDirection])
print('Voyager' if isLoop else maxStep)