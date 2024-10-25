import sys
from collections import deque

# f = open('./input.txt', 'r')
# sys.stdin.readline = f.readline
N, M, K = map(int, sys.stdin.readline().split())
adder = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
trees = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
tree_field = [[deque() for _ in range(N)] for _ in range(N)]
for tree in trees:
    r, c, age = tree
    r, c = r - 1, c - 1
    tree_field[r][c].append(age)

field = [[5 for _ in range(N)] for _ in range(N)]
deads = [[0 for _ in range(N)] for _ in range(N)]
grows = [[0 for _ in range(N)] for _ in range(N)]
d = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
for _ in range(K):
    # spring
    for i in range(N):
        for j in range(N):
            for _ in range(len(tree_field[i][j])):
                tree = tree_field[i][j].popleft()
                if field[i][j] >= tree:
                    field[i][j] -= tree
                    tree_field[i][j].append(tree + 1)
                    if (tree + 1) % 5 == 0: grows[i][j] += 1
                else: deads[i][j] += tree // 2
                
    # summer, fall, winter
    for i in range(N):
        for j in range(N):
            # summer
            field[i][j] += deads[i][j] + adder[i][j]
            deads[i][j] = 0
            
            # fall
            if grows[i][j]:
                for k in range(8):
                    ny, nx = i + d[k][0], j + d[k][1]
                    if 0 <= ny < N and 0 <= nx < N:
                        for _ in range(grows[i][j]): tree_field[ny][nx].appendleft(1)
                grows[i][j] = 0

total = 0
for i in range(N):
    for j in range(N):
        total += len(tree_field[i][j])
print(total)
                