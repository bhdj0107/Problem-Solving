import sys
N = int(sys.stdin.readline())
inp=[]
for _ in range(N):
    tmp = int(sys.stdin.readline())
    inp.append([0, tmp, 0, tmp])
for i in range(N - 1):
    inp[i + 1][0] += max(inp[i][0], inp[i][2])
    inp[i + 1][1] += max(inp[i][0], inp[i][2])
    inp[i + 1][2] += max(inp[i][1], inp[i][3])
    inp[i + 1][3] += inp[i][1]
print(max(inp[-1]))