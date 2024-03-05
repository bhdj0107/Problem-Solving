import sys
fibo = [0, 1]
for i in range(39):
	fibo.append(fibo[-2] + fibo[-1])

T = int(sys.stdin.readline())
for _ in range(T):
	N = int(sys.stdin.readline())
	if N:
		print(fibo[N-1], fibo[N])
	else:
		print(1, 0)
        