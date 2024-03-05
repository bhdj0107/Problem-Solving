import sys
N = int(sys.stdin.readline())
temp = "*"
for _ in range(1, N):
    temp = temp + " *"

for i in range(N):
    if i % 2:
        print(" ", end="")
    print(temp)