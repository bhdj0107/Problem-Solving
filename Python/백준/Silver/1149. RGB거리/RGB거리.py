import sys
N = int(sys.stdin.readline())
inp = []
for _ in range(N):
	inp.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, N):
	inp[i][0] += min(inp[i - 1][1], inp[i - 1][2])
	inp[i][1] += min(inp[i - 1][0], inp[i - 1][2])
	inp[i][2] += min(inp[i - 1][1], inp[i - 1][0])
print(min(inp[-1]))