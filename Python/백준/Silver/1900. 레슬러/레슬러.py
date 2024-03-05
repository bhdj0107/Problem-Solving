import sys
N = int(sys.stdin.readline())
inp = []
for _ in range(N):
    inp.append(tuple(map(int, sys.stdin.readline().split())))

rank = []
for i in range(len(inp)):
    rank.append(((inp[i][1] - 1) / inp[i][0], i))
rank.sort()
for i in range(N - 1, -1, -1):
    print(rank[i][1] + 1)
