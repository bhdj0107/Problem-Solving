import sys
R, C = map(int, sys.stdin.readline().split())
Rg, Cg, Rp, Cp = map(int, sys.stdin.readline().split())

field = []
for _ in range(R): field.append(sys.stdin.readline().rstrip())

coordinate = 0
for i in range(0, R):
    if coordinate != 0: break
    for j in range(0, C):
        if field[i][j] == "P":
            coordinate = (i, j)
            break

for i in range(coordinate[0], coordinate[0] + Rp):
    for j in range(coordinate[1], coordinate[1] + Cp):
        if field[i][j] != "P":
            print(1)
            exit()
print(0)