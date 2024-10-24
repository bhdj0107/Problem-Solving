import sys
input = sys.stdin.readline
from itertools import product
N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
# r, c, d1, d2
probablities = product(range(N - 2), range(1, N - 1), range(1, N), range(1, N))

def whichBlock(pos, N, pivot, d1, d2, region_five):
    pos_r, pos_c = pos
    pivot_r, pivot_c = pivot
    
    if region_five.get(pos_r):
        left, right = region_five.get(pos_r)[0], region_five.get(pos_r)[-1]
        if left <= pos_c <= right: return 5
    
    pos_r += 1
    pos_c += 1
    pivot_r += 1
    pivot_c += 1
    
    if 1 <= pos_r < pivot_r + d1 and 1 <= pos_c <= pivot_c: return 1
    elif 1 <= pos_r <= pivot_r + d2 and pivot_c < pos_c <= N: return 2
    elif pivot_r + d1 <= pos_r <= N and 1 <= pos_c < pivot_c - d1 + d2: return 3
    elif pivot_r + d2 < pos_r <= N and pivot_c - d1 + d2 <= pos_c <= N: return 4

    print(pos, N, pivot, d1, d2)
    print(left, right)
    raise Exception()

ans = 2147483647
for pivot_y, pivot_x, d1, d2 in probablities:
    # 박스를 그릴 수 없는 경우 제외
    if pivot_x - d1 < 0: continue
    if pivot_x + d2 >= N: continue
    if pivot_y + d1 + d2 >= N: continue
    totals = [0 for _ in range(5)]
    
    region_five = {}
    for i in range(d1 + d2 + 1):
        region_five[pivot_y + i] = []
    
    now = (pivot_y, pivot_x)
    
    d = (1, -1)
    for i in range(d1):
        now = (now[0] + d[0], now[1] + d[1])
        region_five[now[0]].append(now[1])
        
    d = (1, 1)
    for i in range(d2):
        now = (now[0] + d[0], now[1] + d[1])
        region_five[now[0]].append(now[1])
        
    d = (-1, 1)
    for i in range(d1):
        now = (now[0] + d[0], now[1] + d[1])
        region_five[now[0]].append(now[1])
    
    d = (-1, -1)
    for i in range(d2):
        now = (now[0] + d[0], now[1] + d[1])
        region_five[now[0]].append(now[1])

    for i in range(N):
        for j in range(N):
            value = field[i][j]
            blockNum = whichBlock((i, j), N, (pivot_y, pivot_x), d1, d2, region_five) - 1
            totals[blockNum] += value

    diff = max(totals) - min(totals)
    if ans > diff: ans = diff
print(ans)