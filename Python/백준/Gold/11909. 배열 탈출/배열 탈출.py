import sys
N = int(sys.stdin.readline())
table = [[float('-inf') for _ in range(N + 1)]]
for _ in range(N):
    table.append([float('-inf')] + list(map(int, sys.stdin.readline().split())))

cost = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

def cost_cal(A, B):
    if A - B < 0:
        return 0
    else:
        return A - B + 1
def a():
    for y in range(1, 2):
        for x in range(2, N + 1):
            cost[y][x] =  min(cost[y - 1][x] + cost_cal(table[y][x], table[y - 1][x]), cost[y][x - 1] + cost_cal(table[y][x], table[y][x - 1]))
    for y in range(2, N + 1):
        for x in range(1, N + 1):
            cost[y][x] =  min(cost[y - 1][x] + cost_cal(table[y][x], table[y - 1][x]), cost[y][x - 1] + cost_cal(table[y][x], table[y][x - 1]))
    print(cost[N][N])
a()