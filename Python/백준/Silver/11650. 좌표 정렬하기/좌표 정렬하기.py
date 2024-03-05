import sys
N = int(sys.stdin.readline())
inp = []
for _ in range(N):
	tmp = tuple(map(int, sys.stdin.readline().split()))
	inp.append(tmp)
inp.sort(key=lambda x:(x[0], x[1]))
for age, name in inp:
	print(age, name)