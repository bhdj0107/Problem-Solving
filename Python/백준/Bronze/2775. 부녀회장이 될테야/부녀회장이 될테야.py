import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    room = [[0 for _ in range(n)] for _ in range(k + 1)]
    for i in range(k + 1):
        room[i][0] = 1
    for i in range(n):
        room[0][i] = i + 1
    for i in range(1, k + 1):
        for j in range(1, n):
            room[i][j] = room[i-1][j] + room[i][j - 1]
    print(room[k][n - 1])