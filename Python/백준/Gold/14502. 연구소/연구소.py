import sys
from itertools import combinations
from collections import deque

N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

zeros = set()
viruses = set()
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0: zeros.add((i, j))
        elif lab[i][j] == 2: viruses.add((i, j))
ans = -1
d = ((1, 0), (0, 1), (-1, 0), (0, -1))
ans_walls = set()
ans_visited = set()
for walls in combinations(zeros, 3):
    # 벽 막기
    for wall in walls:
        y, x = wall
        lab[y][x] = 1
    
    visited = set()
    q = deque([*viruses])
    while q:
        now = q.popleft()
        if now in visited: continue
        else:
            visited.add(now)
            for i in range(4):
                ny = now[0] + d[i][0]
                nx = now[1] + d[i][1]
                if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
                if lab[ny][nx] == 0 and (ny, nx) not in visited:
                    q.append((ny, nx))
    # 벽 풀기
    for wall in walls:
        y, x = wall
        lab[y][x] = 0
    cnt = len(zeros) - len(visited) + len(viruses) - 3
    if ans < cnt:
        ans = cnt
        ans_walls = walls
        ans_visited = visited
        
print(ans)        