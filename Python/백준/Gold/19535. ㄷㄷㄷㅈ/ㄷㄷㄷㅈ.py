import sys
N = int(sys.stdin.readline())
tree = [0 for _ in range(N + 1)]
inp = []
for _ in range(N - 1):
    inp.append(tuple(map(int, sys.stdin.readline().split())))
    tree[inp[-1][0]] += 1
    tree[inp[-1][1]] += 1
d_cnt, g_cnt = 0, 0
for a,b in inp:
    d_cnt += (tree[a] - 1) * (tree[b] - 1)
for c in tree[1:]:
    if c >= 3:
        g_cnt += c*(c-1)*(c-2)//6
if g_cnt * 3 < d_cnt:
    print('D')
if g_cnt * 3 > d_cnt:
    print('G')
if g_cnt * 3 == d_cnt:
    print('DUDUDUNGA')