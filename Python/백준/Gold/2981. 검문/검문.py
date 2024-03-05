import sys
N = int(sys.stdin.readline())
def gcd(a, b):
	c, d = max(a,b), min(a,b)
	while d:
		r = c % d
		c, d = d, r
	return c

first = int(sys.stdin.readline())
final_gcd = abs(first - int(sys.stdin.readline()))
for _ in range(N - 2):
	final_gcd = gcd(final_gcd, abs(first - int(sys.stdin.readline())))

head = []
root = int(final_gcd ** 0.5)
for i in range(2, root + 1):
	if final_gcd % i == 0:
		head.append(str(i))

for i in range(len(head) - 1, -1, -1):
	tmp = final_gcd // int(head[i])
	if tmp != int(head[i]):
		head.append(str(tmp))
head.append(str(final_gcd))
print(" ".join(head))