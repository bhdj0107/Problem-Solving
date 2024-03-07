import sys
N, M = map(int, sys.stdin.readline().split())
A = tuple(map(int, sys.stdin.readline().split()))
B = tuple(map(int, sys.stdin.readline().split()))

print(sum(A)+sum(B))