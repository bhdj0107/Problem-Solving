import sys
N = int(sys.stdin.readline())
inp = []
for _ in range(N):
	tmp = tuple(sys.stdin.readline().split())
	inp.append(tmp)
inp.sort(key=lambda x:int(x[0]))
for age, name in inp:
	print(age, name)