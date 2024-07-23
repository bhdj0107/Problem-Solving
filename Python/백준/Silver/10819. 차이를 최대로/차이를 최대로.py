import sys
from itertools import permutations

N = int(sys.stdin.readline())
inps = list(map(int, sys.stdin.readline().split()))
ans = -1
for idxes in permutations(range(len(inps)), len(inps)):
    tmp = sum([abs(inps[idxes[i]] - inps[idxes[i + 1]]) for i in range(len(inps) - 1)])
    ans = max(ans, tmp)
print(ans)