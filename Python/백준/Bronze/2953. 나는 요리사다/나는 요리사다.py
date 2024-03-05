import sys
idx, temp = 0,0
for i in range(5):
    a = sum(map(int,sys.stdin.readline().split()))
    if a > temp:
        temp = a
        idx = i
print(idx + 1, temp)