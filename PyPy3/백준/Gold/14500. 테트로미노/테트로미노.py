import sys
from itertools import product, combinations
N, M = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cumField = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        cumField[i + 1][j + 1] = cumField[i + 1][j] + cumField[i][j + 1] + field[i][j] - cumField[i][j]

ans = 0
# 가로 길쭉이 검사
for i in range(N):
    for j in range(M - 3):
        tmpSum = cumField[i + 1][j + 4] - cumField[i][j + 4] - cumField[i + 1][j] + cumField[i][j]
        ans = max(ans, tmpSum)

for i in range(N - 3):
    for j in range(M):
        tmpSum = cumField[i + 4][j + 1] - cumField[i + 4][j] - cumField[i][j + 1] + cumField[i][j]
        ans = max(ans, tmpSum)

# 나머지 검사 (가로 3, 세로 2)
for i in range(N - 1):
    for j in range(M - 2):
        tmpBlock = cumField[i + 2][j + 3] - cumField[i][j + 3] - cumField[i + 2][j] + cumField[i][j]
        pts = combinations(product(range(2), range(3)), 2)
        skips = (((0,1), (1, 1)), ((1, 0), (0, 1)), ((1, 1), (0, 2)), ((0,0), (1, 1)), ((0, 1), (1, 2)))
        for pt in pts:
            skip = False
            for skip_a, skip_b in skips:
                if skip_a in pt and skip_b in pt: 
                    skip = True
                    break
            if skip: continue
            pt1, pt2 = pt
            field1 = field[i + pt1[0]][j + pt1[1]]
            field2 = field[i + pt2[0]][j + pt2[1]]
            tmpMinus = field1 + field2
            ans = max(ans, tmpBlock - tmpMinus)

# 나머지 검사 (가로 2, 세로 3)
for i in range(N - 2):
    for j in range(M - 1):
        tmpBlock = cumField[i + 3][j + 2] - cumField[i][j + 2] - cumField[i + 3][j] + cumField[i][j]
        pts = combinations(product(range(3), range(2)), 2)
        skips = (((1,0), (1, 1)), ((0, 1), (1, 0)), ((1, 1), (2, 0)), ((0,0), (1, 1)), ((1, 0), (2, 1)))
        for pt in pts:
            skip = False
            for skip_a, skip_b in skips:
                if skip_a in pt and skip_b in pt: 
                    skip = True
                    break
            if skip: continue
            pt1, pt2 = pt
            field1 = field[i + pt1[0]][j + pt1[1]]
            field2 = field[i + pt2[0]][j + pt2[1]]
            tmpMinus = field1 + field2
            ans = max(ans, tmpBlock - tmpMinus)

print(ans)