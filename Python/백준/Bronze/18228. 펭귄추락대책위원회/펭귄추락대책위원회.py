import sys
N = int(sys.stdin.readline())
ice = list(map(int, sys.stdin.readline().split()))
print(min(ice[:ice.index(-1)]) + min(ice[ice.index(-1) + 1:]))