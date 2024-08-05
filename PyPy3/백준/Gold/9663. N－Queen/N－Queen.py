import sys

N = int(sys.stdin.readline())

cols = [False for _ in range(N)]
rows = [False for _ in range(N)]
rightTop = [False for _ in range(2 * N - 1)]
rightBottom = [False for _ in range(2 * N - 1)]

def setQueen(i, j):
    global rows, cols, rightTop, rightBottom
    rows[i] = True
    cols[j] = True
    rightTop[i + j] = True
    rightBottom[N - 1 - i + j] = True

def unsetQueen(i, j):
    global rows, cols, rightTop, rightBottom
    rows[i] = False
    cols[j] = False
    rightTop[i + j] = False
    rightBottom[N - 1 - i + j] = False

def canSetQueen(i, j):
    if rows[i]: return False
    if cols[j]: return False
    if rightTop[i + j]: return False
    if rightBottom[N - 1 - i + j]: return False
    return True


cnt = 0
def backtracking(D):
    global cnt
    if D == N:
        cnt += 1
        return
    for i in range(N):
        if canSetQueen(D, i):
            setQueen(D, i)
            backtracking(D + 1)
            unsetQueen(D, i)

for i in range(N):
    setQueen(0, i)
    backtracking(1)
    unsetQueen(0, i)

print(cnt)