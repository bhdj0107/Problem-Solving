import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    if N >= 12 and M >= 4:
        print(11 * M + 4)
    else:
        print(-1)