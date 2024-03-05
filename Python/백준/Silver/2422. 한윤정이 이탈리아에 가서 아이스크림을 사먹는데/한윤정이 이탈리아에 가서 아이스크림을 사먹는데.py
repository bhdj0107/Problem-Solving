import sys
N, M = map(int, sys.stdin.readline().split())
sample = [[] for _ in range(N)]

cnt = 0
for _ in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    sample[temp[0] - 1].append(temp[1] - 1)

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if i in sample[j] or i in sample[k]:
                continue
            if j in sample[i] or j in sample[k]:
                continue
            if k in sample[j] or k in sample[i]:
                continue
            cnt += 1

print(cnt)