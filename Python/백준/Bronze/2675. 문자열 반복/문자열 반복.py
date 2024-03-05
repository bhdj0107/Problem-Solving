import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, S = sys.stdin.readline().split()
    for c in S:
        print(c * int(N),end='')
    print("")