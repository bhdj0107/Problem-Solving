import sys
A, B, C = map(int, sys.stdin.readline().split())
A1 = A * B / C
A2 = A / B * C
print(int(max(A1, A2)))