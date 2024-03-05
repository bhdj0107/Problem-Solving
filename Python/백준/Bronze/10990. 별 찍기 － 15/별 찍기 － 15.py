import sys
N = int(sys.stdin.readline())

for _ in range(1, N):
    print(" ", end="")
print("*")

for i in range(1, N):
    for _ in range(N - 1 - i):
        print(" ", end="")
    print("*", end="")
    
    for _ in range(1 + (2 * (i - 1))):
        print(" ", end="")
    print("*")