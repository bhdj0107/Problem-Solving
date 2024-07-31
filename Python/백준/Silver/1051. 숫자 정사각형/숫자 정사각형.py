import sys
from itertools import product
N, M = map(int, sys.stdin.readline().split())
field = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

def chkBox(field, pt, size):
    top, left = pt
    bottom, right = top + size - 1, left + size - 1
    value = field[top][left]
    if bottom < N and right < M:
        pts = ((top, left), (top, right), (bottom, left), (bottom, right))
        for (y, x) in pts:
            if field[y][x] != value: return False
        return True
    else:
        return False
    
ans = None
currentSize = min(N, M)

while True:
    for i in range(N - currentSize + 1):
        for j in range(M - currentSize + 1):
            prob = (i, j)
            chk = chkBox(field, prob, currentSize)
            if chk:
                ans = currentSize
                break
        if ans: break
    if ans: break
    else: currentSize -= 1

print(ans * ans)