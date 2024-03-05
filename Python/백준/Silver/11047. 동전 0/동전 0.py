import sys
N, K = map(int, sys.stdin.readline().split())
inp = []
for _ in range(N):
	tmp = int(sys.stdin.readline())
	if tmp <= K:
		inp.append(tmp)
cnt = 0
for i in range(len(inp) - 1, -1, -1):
	if K >= inp[i]:
		tmp = K // inp[i]
		K -= inp[i] * tmp
		cnt += tmp
print(cnt)