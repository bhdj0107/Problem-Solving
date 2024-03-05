import sys
def a():
    N, M = map(int, sys.stdin.readline().split())
    field = [tuple() for _ in range(N + 1)]
    field[0] = tuple(0 for _ in range(M + 1))
    for i in range(1, N + 1):
        temp = tuple(map(int, sys.stdin.readline().split()))
        inp = [0 for _ in range(M + 1)]
        for j in range(1, M+1):
            inp[j] = inp[j-1] + temp[j-1]
        field[i] = (0,) + tuple(field[i-1][j] + inp[j] for j in range(1, M + 1))
    K = int(sys.stdin.readline())
    for _ in range(K):
        y1, x1, y2, x2 = map(int,sys.stdin.readline().split())
        print(field[y2][x2] - field[y2][x1 - 1] - field[y1 - 1][x2] + field[y1 - 1][x1 - 1])
a()