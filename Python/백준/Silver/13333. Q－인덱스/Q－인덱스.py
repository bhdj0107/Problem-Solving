import sys
N = int(sys.stdin.readline())
inp = tuple(map(int, sys.stdin.readline().split()))
cnt = [0 for _ in range(N + 1)]
for n in inp:
    if n > N:
        cnt[N] += 1
    else:
        cnt[n] += 1
temp = [0 for _ in range(N + 1)]
for i in range(N + 1):
    temp[i] = cnt[i]
for i in range(N, 0, -1):
    cnt[i - 1] += cnt[i]


for i in range(N + 1):
    if cnt[i] >= i and N - cnt[i] + temp[i] >= N - i:
        print(i)
        exit()