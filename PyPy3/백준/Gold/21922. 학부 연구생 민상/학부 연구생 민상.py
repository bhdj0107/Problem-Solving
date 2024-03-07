# 2020 07 01 1944 start
# 2020 07 01 2013 break
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

wind = [[0 for _ in range(M)] for _ in range(N)]

aircon_set = set()
for i in range(N):
    for j in range(M):
        if field[i][j] == 9:
            aircon_set.add((i, j))


def bfs():
    global wind
    # Direction 1, 2, 3, 4 순서대로 상, 하, 좌, 우 이다
    queue = deque()
    after = {}
    after[0] = [0, 1, 2, 3, 4]
    after[1] = [0, 1, 2, 0, 0]
    after[2] = [0, 0, 0, 3, 4]
    after[3] = [0, 4, 3, 2, 1]
    after[4] = [0, 3, 4, 1, 2]
    after[9] = [0, 0, 0, 0, 0]
    for y, x in aircon_set:
        wind[y][x] = 1
        for dy, dx, d in ((1, 0, 2), (0, 1, 4), (-1, 0, 1), (0, -1, 3)):
            if 0 <= y + dy < N and 0 <= x + dx < M:
                queue.append((d, y + dy, x + dx))
    while queue:
        d, y, x = queue.popleft()
        if 0 <= y < N and 0 <= x < M:
            wind[y][x] = 1
            after_d = after[field[y][x]][d]
            if after_d == 1:
                queue.append((1, y - 1, x))
            elif after_d == 2:
                queue.append((2, y + 1, x))
            elif after_d == 3:
                queue.append((3, y, x - 1))
            elif after_d == 4:
                queue.append((4, y, x + 1))
bfs()
ans = 0
for i in wind:
    ans += sum(i)
print(ans)