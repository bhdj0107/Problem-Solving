import sys
N = int(sys.stdin.readline())
a, b = 0, 1
for i in range(N - 1):
	c = a+b
	a, b = b, c
print(b)