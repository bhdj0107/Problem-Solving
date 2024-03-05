import sys
A = list(map(int, sys.stdin.readline().split()))
A.sort()
print(A[0], A[1], A[2])