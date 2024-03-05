import sys
from collections import deque

def asd():
    mx = 0
    cnt = 0
    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)
    queue = deque()
    N, M = map(int, sys.stdin.readline().split())
    field = []
    for _ in range(N):
        field.append(list(map(int, sys.stdin.readline().split())))
    
    for y in range(N):
        for x in range(M):
            size = 0
            if field[y][x] == 1:
                cnt += 1
                size += 1
                field[y][x] = 0
                for d in range(4):
                    queue.append((x + dx[d], y + dy[d]))
    
                while queue:
                    tx, ty = queue.popleft()
                    if tx < 0 or ty < 0 or tx >= M or ty >= N:
                        continue
                    if field[ty][tx] == 1:
                        size += 1
                        field[ty][tx] = 0
                        for d in range(4):
                            queue.append((tx + dx[d], ty + dy[d]))
    
                mx = max(size, mx)
    
    print(cnt)
    print(mx)
    
asd()