import sys
R, C = map(int, sys.stdin.readline().split())
ans = [["!" for _ in range(2 * C)] for _ in range(2 * R)]
swap = {"#" : ".", "." : "#"}
for i in range(R):
    inp = sys.stdin.readline()
    for j in range(C):
        ans[i][j] = inp[j]
        ans[i][2 * C - 1 - j] = inp[j]
        ans[2 * R - 1 - i][j] = inp[j]
        ans[2 * R - 1 - i][2 * C - 1 - j] = inp[j]

y, x = map(int, sys.stdin.readline().split())
ans[y - 1][x - 1] = swap[ans[y - 1][x - 1]]

for i in ans:
    print("".join(i))