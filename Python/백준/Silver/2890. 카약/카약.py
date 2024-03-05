import sys
R, C = map(int, sys.stdin.readline().split())
dist = [0 for _ in range(9)]
rank = [0 for _ in range(9)]
kayak = tuple(str(i * 111) for i in range(1, 10))
for i in range(R):
    inp = sys.stdin.readline().rstrip()
    for j in kayak:
        if j in inp:
            dist[(int(j) // 111) - 1] = len(inp.split(j)[1])
cnt = 1
for i in range(51):
    chk = False
    for j in range(9):
        if dist[j] == i:
            chk = True
            rank[j] = cnt
    if chk:
        cnt += 1

for i in rank:
    print(i)
