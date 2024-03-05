import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
field = []
for _ in range(N):
    field.append(list(map(int, sys.stdin.readline().split())))

# 빙산 좌표 미리 기록
ice = {}
for i in range(N):
    for j in range(M):
        if field[i][j]: ice[(i, j)] = field[i][j]

# 녹이기
def melt():
    global field, ice
    # 각 얼음 주변의 물 계산
    tmp = {}
    for y, x in ice:
        tmp[(y, x)] = 0
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if 0 <= y + dy < N and 0 <= x + dx < M:
                tmp[(y, x)] += int(field[y + dy][x + dx] == 0)
    
    # 계산 값을 기준으로 얼음을 녹인다
    # 얼음이 다 녹으면 기록된 좌표를 삭제한다.
    queue = list(ice.keys())
    for y, x in queue:
        field[y][x] = max(ice[(y, x)] - tmp[(y, x)], 0)
        if field[y][x] == 0:
            del ice[(y, x)]
        else:
            ice[(y, x)] = field[y][x]

# 덩어리 구분하기
def block():
    # ice 를 tmp 에 깊은 복사 하여, 시작 좌표로 부터 bfs를 수행하며 좌표를 tmp
    # 에서 지워나가고, tmp에 남은 좌표가 있다면 두 덩어리 이상
    tmp = dict(ice)
    start = list(tmp.keys())[0]
    queue = deque()
    queue.append(start)
    del tmp[start]
    while queue:
        pos = queue.popleft()
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            y, x = pos[0] + dy, pos[1] + dx
            if 0 <= y < N and 0 <= x < M:
                if (y, x) in tmp.keys():
                    del tmp[(y, x)]
                    queue.append((y, x))
    return bool(tmp)

melt()
cnt = 0
while True:
    cnt += 1
    if block(): break
    melt()
    if not ice:
        cnt = 0
        break

print(cnt)