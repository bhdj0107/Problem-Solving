import sys
N = int(sys.stdin.readline())
car = tuple(map(int, sys.stdin.readline().split()))
cnt = 0
for i in car:
    if i == N:
        cnt += 1
print(cnt)