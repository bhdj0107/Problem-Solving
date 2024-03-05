import sys

cnt = 0
block = [0 for _ in range(7)]

block[0] = [[0], [0, 0, 0, 0]]
block[1] = [[0, 0]]
block[2] = [[0, -1], [0, 0, 1]]
block[3] = [[0, -1, -1], [0, 1]]
block[4] = [[0, -1, 0], [0, 0, 0], [0, -1], [0, 1]]
block[5] = [[0, 0, 0], [0, 1, 1], [0, -2], [0, 0]]
block[6] = [[0, 0], [0, 0, 0], [0, 0, -1], [0, 2]]

C, P = map(int, sys.stdin.readline().split())
field = tuple(map(int, sys.stdin.readline().split()))

for i in block[P - 1]:
    for j in range(1 + C - len(i)):
        temp = field[j]
        for k in range(len(i)):
            if not field[j + k] - temp == i[k]:
                break
            else:
                if k == len(i) - 1:
                    cnt += 1

print(cnt)