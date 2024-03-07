import sys
N, T = map(int, sys.stdin.readline().split())

T = (T - 1) % (4 * N - 2)
if T < 2 * N - 1:
    print(T + 1)
else:
    print(4 * N - 1 - T)