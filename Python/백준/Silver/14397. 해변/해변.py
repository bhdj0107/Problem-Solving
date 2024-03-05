import sys
N, M = map(int, sys.stdin.readline().split())
inp = ["".join(["@" for _ in range(M + 2)])]
for _ in range(N):
    inp.append("@" + sys.stdin.readline().rstrip() + "@")
inp.append("".join(["@" for _ in range(M + 2)]))
cnt = 0
dx = ((0, 1, -1, 1, 0, 1), (-1, 0, -1, 1, -1, 0))
dy = (-1, -1, 0, 0, 1, 1)
for i in range(1, N + 1):
    for j in range(1, M + 1):
        temp = inp[i][j]
        if temp == "#":
            for k in range(6):
                if inp[i + dy[k]][j + dx[i % 2][k]] == '.':
                    cnt += 1
print(cnt)