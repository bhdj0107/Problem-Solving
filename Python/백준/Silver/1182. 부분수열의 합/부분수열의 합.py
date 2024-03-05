import sys
def asd():
    cnt = 0
    N, S = map(int, sys.stdin.readline().split())
    count = [[] for _ in range(N)]
    inp = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        count[i].append(inp[i])
    
    for i in range(N - 1):
        for j in range(i + 1, N):
            temp = []
            for k in count[j]:
                temp.append(k + count[i][0])
            count[j].extend(temp)
    
    for i in range(N):
        cnt += count[i].count(S)
    print(cnt)

asd()