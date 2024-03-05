import sys
N = int(sys.stdin.readline())
peoples = {i + 1:[] for i in range(N)}
Distance_Table = [[60 for _ in range(N)] for _ in range(N)]
for i in range(N):
    Distance_Table[i][i] = 0
while 1:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break
    Distance_Table[a - 1][b - 1] = 1
    Distance_Table[b - 1][a - 1] = 1
    peoples[a].append(b)
    peoples[b].append(a)
for n in range(N):
    for i in range(N):
        for j in range(N):
            if i == n or j == n or i == j:
                continue
            else:
                if Distance_Table[i][j] > Distance_Table[i][n] + Distance_Table[n][j]:
                    Distance_Table[i][j] = Distance_Table[i][n] + Distance_Table[n][j]
m = 60
ans = []
for i in range(N):
    if max(Distance_Table[i]) < m:
        m = max(Distance_Table[i])
        ans = [i + 1]
    elif max(Distance_Table[i]) == m:
        ans.append(i + 1)
print(m, len(ans))
for i in ans[:-1]:
    print(i, end=" ")
print(ans[-1])