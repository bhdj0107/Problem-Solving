import sys
T = int(sys.stdin.readline())
for _ in range(T):
	N, J = map(int, sys.stdin.readline().split())
	inp = []
	for _ in range(J):
		a, b = map(int, sys.stdin.readline().split())
		inp.append(a* b)
	inp.sort()
	cnt = 0
	while N > 0:
		cnt += 1
		N -= inp.pop()
	print(cnt)
