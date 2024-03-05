import sys
N = int(sys.stdin.readline())
inp = []
for _ in range(N):
    inp.append(tuple(map(int, sys.stdin.readline().split())))
    
inp.sort()
cnt = 1
for i in range(1, N):
    A = tuple(map(lambda x : x[1], inp[:i]))
    if min(A) > inp[i][1]:
        cnt += 1

print(cnt)