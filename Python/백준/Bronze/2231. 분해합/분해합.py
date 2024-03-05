import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    tmp = i
    for j in str(tmp):
        tmp += int(j)
    if tmp == N:
        print(i)
        exit()
print(0)