import sys
def GCD(a, b):
    if a < b:
        a, b = b, a
    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r

N = int(sys.stdin.readline())
for _ in range(N):
    M = -1
    table = tuple(map(int, sys.stdin.readline().split()))
    for i in range(len(table) - 1):
        for j in range(i + 1, len(table)):
            M = max(M, GCD(table[i], table[j]))
    print(M)