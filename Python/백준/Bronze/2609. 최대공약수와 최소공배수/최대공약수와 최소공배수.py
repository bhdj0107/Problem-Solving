import sys
A, B = map(int, sys.stdin.readline().split())

# GCD(a,b) = GCD(b,r)
# r = a % b
a, b = A, B
while b:
    a, b = b, a % b
print(a)

# lcm(A, B) = A * B / GCD(A, B)
print(A*B//a)