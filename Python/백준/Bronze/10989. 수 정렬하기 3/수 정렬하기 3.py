import sys
N = int(sys.stdin.readline())
cnt = [0 for i in range(10001)]
for _ in range(N):
	cnt[int(sys.stdin.readline())] += 1
for i in range(1, 10001):
	for _ in range(cnt[i]):
		print(i)