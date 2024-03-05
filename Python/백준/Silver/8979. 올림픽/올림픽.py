import sys
N, T = map(int, sys.stdin.readline().split())
cnt = 1
target = (-1, -1, -1)
medal = {}

for _ in range(N):
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[1] not in medal.keys():
        medal[inp[1]] = {}
    if inp[2] not in medal[inp[1]].keys():
        medal[inp[1]][inp[2]] = {}
    if inp[3] not in medal[inp[1]][inp[2]].keys():
        medal[inp[1]][inp[2]][inp[3]] = set()
    medal[inp[1]][inp[2]][inp[3]].add(inp[0])
    if inp[0] == T:
        target = (inp[1], inp[2], inp[3])

for G in medal.keys():
    if G < target[0]:
        continue
    for S in medal[G].keys():
        if G == target[0] and S < target[1]:
            continue
        for B in medal[G][S].keys():
            if G == target[0] and S == target[1] and B <= target[2]:
                continue
            cnt += len(medal[G][S][B])

print(cnt)