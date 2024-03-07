import sys
N, M = map(int, sys.stdin.readline().split())
K = list(map(int, sys.stdin.readline().split()))
counts = {}
for i in K:
    j = i
    while j <= N:
        counts[j] = True
        j += i
print(sum(counts.keys()))
        