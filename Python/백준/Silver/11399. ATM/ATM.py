import sys
N = int(sys.stdin.readline())
inp = list(map(int, sys.stdin.readline().split()))
inp.sort()
for i in range(N):
	inp[i] *= N - i
print(sum(inp))
