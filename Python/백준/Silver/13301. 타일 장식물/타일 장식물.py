import sys
a, b = 1, 1
N = int(sys.stdin.readline())

if N == 1:
    print(4)
    exit()
if N == 2:
    print(6)
    exit()

for _ in range(N - 2):
    c = a + b
    a, b = b, c

print((a+b+b)*2)