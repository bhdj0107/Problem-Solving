import sys
from itertools import product
N = int(sys.stdin.readline())

def switcher(chr):
    if chr == 'P': return 0
    elif chr == 'C': return 1
    elif chr == 'Z': return 2
    elif chr == 'Y': return 3

field = [list(map(switcher, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

def chkLine(idx, isRow):
    maxCnt = 1
    if isRow:
        currentCnt = 1
        for i in range(1, N):
            if field[idx][i] != field[idx][i - 1]:
                maxCnt = max(maxCnt, currentCnt)
                currentCnt = 1
            else: currentCnt += 1
        maxCnt = max(maxCnt, currentCnt)
    else:
        currentCnt = 1
        for i in range(1, N):
            if field[i][idx] != field[i - 1][idx]:
                maxCnt = max(maxCnt, currentCnt)
                currentCnt = 1
            else: currentCnt += 1
        maxCnt = max(maxCnt, currentCnt)
    return maxCnt

maxEdibleCnt = 1
for i in range(N):
    for j in range(N):
        if j < N - 1:
            field[i][j], field[i][j + 1] = field[i][j + 1], field[i][j]
            maxEdibleCnt = max(maxEdibleCnt, chkLine(i, True), chkLine(j, False), chkLine(j + 1, False))
            field[i][j], field[i][j + 1] = field[i][j + 1], field[i][j]
        if i < N - 1:
            field[i][j], field[i + 1][j] = field[i + 1][j], field[i][j]
            maxEdibleCnt = max(maxEdibleCnt, chkLine(j, False), chkLine(i, True), chkLine(i + 1, True))
            field[i][j], field[i + 1][j] = field[i + 1][j], field[i][j]
print(maxEdibleCnt)
