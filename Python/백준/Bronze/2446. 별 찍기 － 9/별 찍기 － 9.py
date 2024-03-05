import sys
N = int(sys.stdin.readline())
for i in range(N):
    for _ in range(i):
        print(" ", end="")
    for _ in range(2 * N - 1 - 2 * i):
        print("*", end="")
    print("")
for i in range(N-2,-1,-1):
    for _ in range(i):
        print(" ", end="")
    for _ in range(2 * N - 1 - 2 * i):
        print("*", end="")
    print("")