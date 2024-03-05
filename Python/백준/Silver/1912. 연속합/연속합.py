import sys
N = int(sys.stdin.readline())
inp = list(map(int, sys.stdin.readline().split()))
ans = inp[0]
for i in range(1, N):
	inp[i] = max(inp[i - 1] + inp[i], inp[i])
	ans = max(inp[i], ans)
print(ans)