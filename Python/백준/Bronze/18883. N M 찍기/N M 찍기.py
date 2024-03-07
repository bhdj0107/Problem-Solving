import sys
N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    for j in range(M - 1):
        print(i * M + j + 1, end=' ')
    print(i * M + M)