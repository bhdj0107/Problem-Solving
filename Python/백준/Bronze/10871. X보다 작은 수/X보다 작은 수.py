import sys
N, X = map(int, sys.stdin.readline().split())
inp = tuple(map(int, sys.stdin.readline().split()))
for i in inp[:-1]:
  if i < X:
    print(i, end=" ")
if X > inp[-1]:
    print(inp[-1])