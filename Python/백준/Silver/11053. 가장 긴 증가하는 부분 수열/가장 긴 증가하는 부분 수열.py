import sys
N = int(sys.stdin.readline())
inp = list(map(int,sys.stdin.readline().split()))
cnt = [0 for _ in range(N)]
cnt[0] = 1
for i in range(1, N):
	M = 0
	for j in range(0, i):
		if inp[i] > inp[j]:
			M = max(M, cnt[j])
	cnt[i] = M + 1
print(max(cnt))