# 2021 06 30 2210 start
import sys
from collections import deque
W, H = map(int, sys.stdin.readline().split())
field = []

# '외부' 처리의 효율성을 위해 데이터에 가장자리를 공백으로 두른다
field.append(tuple([0 for _ in range(W + 2)]))
for _ in range(H):
    field.append(tuple([0] + list(map(int, sys.stdin.readline().split())) + [0]))
field.append(tuple([0 for _ in range(W + 2)]))

# 가장자리에서 bfs를 실시하여 내부와 외부를 flag에 저장한다
flag = [[1 for _ in range(W + 2)] for _ in range(H + 2)]
def bfs():
    global flag
    chk = set()
    queue = deque()
    queue.append((0, 0))
    while queue:
        y, x = queue.popleft()
        if (y, x) in chk:
            continue
        chk.add((y, x))
        flag[y][x] = 0
        if y % 2:
            for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1)):
                if 0 <= y + dy <= H + 1 and 0 <= x + dx <= W + 1:
                    if not field[y + dy][x + dx]: queue.append((y + dy, x + dx))
        else:
            for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, -1)):
                if 0 <= y + dy <= H + 1 and 0 <= x + dx <= W + 1:
                    if not field[y + dy][x + dx]: queue.append((y + dy, x + dx))

# 각 내부 칸에 대하여 주변의 외부칸 갯수 총합이 벽의 길이
def count():
    ans = 0
    for y in range(1, H + 1):
        for x in range(1, W + 1):
            if flag[y][x]:
                # 만약 홀수번째 줄이라면
                if y % 2:
                    for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1)):
                        if 0 <= y + dy <= H + 1 and 0 <= x + dx <= W + 1:
                            ans += int(not flag[y + dy][x + dx])
                else:
                    for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, -1)):
                        if 0 <= y + dy <= H + 1 and 0 <= x + dx <= W + 1:
                            ans += int(not flag[y + dy][x + dx])
    return ans
bfs()
print(count())