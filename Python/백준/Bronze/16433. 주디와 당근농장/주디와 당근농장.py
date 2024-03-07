import sys
N, R, C = map(int, sys.stdin.readline().split())
temp = {0:"", 1:""}
if (R + C) % 2:
    for i in range(N):
        if i % 2:
            temp[0] = temp[0] + "v"
            temp[1] = temp[1] + "."
        else:
            temp[0] = temp[0] + "."
            temp[1] = temp[1] + "v"
else:
    for i in range(N):
        if not i % 2:
            temp[0] = temp[0] + "v"
            temp[1] = temp[1] + "."
        else:
            temp[0] = temp[0] + "."
            temp[1] = temp[1] + "v"

for i in range(N):
    print(temp[i%2])