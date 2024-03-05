import sys
T = int(sys.stdin.readline())
for _ in range(T):
    gcd_sum = 0
    inp = tuple(map(int, sys.stdin.readline().split()))
    for i in range(1, len(inp) - 1):
        for j in range(i + 1, len(inp)):
            a, b = inp[i], inp[j]
            while b:
                a, b = b, a % b
            gcd_sum += a
    print(gcd_sum)