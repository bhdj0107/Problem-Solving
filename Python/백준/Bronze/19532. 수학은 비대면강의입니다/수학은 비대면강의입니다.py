import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split())
x, y = 0, 0

A = a * d
B = b * d
C = c * d

D = d * a
E = e * a
F = f * a

B = B - E
C = C - F

y = C // B

A = a * e
B = b * e
C = c * e

D = d * b
E = e * b
F = f * b

A = A - D
C = C - F

x = C // A

print(x, y)