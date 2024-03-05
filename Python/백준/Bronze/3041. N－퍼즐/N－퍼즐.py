import sys
dict = {}
temp = 65
for i in range(4):
    for j in range(4):
        dict[chr(temp)] = (i, j)
        temp += 1

inp = []
for _ in range(4):
    inp.append(sys.stdin.readline().rstrip())

ans = 0
for i in range(4):
    for j in range(4):
        if inp[i][j] != '.':
            ans += abs(dict[inp[i][j]][0] - i) + abs(dict[inp[i][j]][1] - j)

print(ans)