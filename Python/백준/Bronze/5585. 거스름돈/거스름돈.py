import sys
N = 1000 - int(sys.stdin.readline())
ans = 0
while N:
	for i in (500, 100, 50, 10, 5, 1):
		if N >= i:
			N -= i
			ans += 1
			break
print(ans)
