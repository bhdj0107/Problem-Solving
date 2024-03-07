import sys
K, N = map(int, sys.stdin.readline().split())
dic = set()
inp = tuple(map(int, sys.stdin.readline().split()))
for i in range(N - 1):
    for j in range(i + 1, N):
        dic.add((inp[i], inp[j]))

for i in range(K - 1):
    inp = tuple(map(int, sys.stdin.readline().split()))
    minus = set()
    for j in range(N - 1, 0, -1):
        for k in range(j - 1, -1, -1):
            minus.add((inp[j], inp[k]))
    dic = dic - minus
print(len(dic))