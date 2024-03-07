# 2020 07 02 1900 start
import sys
N, X, K = map(int, sys.stdin.readline().split())
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    if a == X: X = b
    elif b == X: X = a
print(X)