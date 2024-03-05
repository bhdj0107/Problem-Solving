import sys
input = sys.stdin.readline
N, M = map(int, input().split())
inp = []
for _ in range(N):
    inp.append(input().rstrip())
    
tok = {'A':0, 'C':1, 'G':2, 'T':3, 0:"A", 1:'C', 2:'G', 3:'T'}
cnt = [[0,0,0,0] for _ in range(M)]
for i in range(N):
    for j in range(M):
        cnt[j][tok[inp[i][j]]] += 1
ans = 0
for i in range(M):
    mx = -1
    idx = -1
    for j in range(3, -1, -1):
        if mx <= cnt[i][j]:
            mx = cnt[i][j]
            idx = j
    ans += N - mx
    print(tok[idx], end='')
print()
print(ans)
        

