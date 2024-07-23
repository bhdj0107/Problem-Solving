import sys
from itertools import product
from math import inf
R, C = map(int, sys.stdin.readline().split())
field = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
nextField = [field[i].copy() for i in range(R)]

left, top, right, bottom = inf, inf, -1, -1
def isShrink(y, x):
    nPoses = [(y + i[0], x + i[1]) for i in ((-1, 0), (0, -1), (1, 0), (0, 1))]
    cnt = 0
    for ny, nx in nPoses:
        if ny >= 0 and ny < R and nx >= 0 and nx < C:
            if field[ny][nx] == '.': cnt += 1
        else: cnt += 1
    return cnt >= 3

for i in range(R):
    for j in range(C):
        if field[i][j] == 'X':
            if not isShrink(i, j):
                left = min(left, j)
                top = min(top, i)
                right = max(right, j)
                bottom = max(bottom, i)
            else:
                nextField[i][j] = '.'

for i in range(top, bottom + 1):
    print("".join(nextField[i][left:right+1]))