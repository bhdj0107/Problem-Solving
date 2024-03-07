import sys
N, M, H = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
milk = {}
for i in range(N):
    for j in range(N):
        if field[i][j] == 1:
            home = (i, j)
        elif field[i][j] == 2:
            milk[len(milk) + 1] = (i, j)
milk[len(milk) + 1] = home
milk[0] = home
dist = [[-1 for _ in range(len(milk))] for _ in range(len(milk))]
for i in range(len(milk)):
    for j in range(len(milk)):
        dist[i][j] = abs(milk[i][0] - milk[j][0]) + abs(milk[i][1] - milk[j][1])
visited = [False for _ in range(len(milk))]
last = 0
max_cnt = -1

def dfs(D):
    global visited, last, max_cnt, M
    for i in range(1, len(milk)):
        if visited[i]:
            continue
        else:
            if M >= dist[last][i]:
                if i == len(milk) - 1:
                    max_cnt = max(max_cnt, D)
                    return
                visited[i] = True
                prev_M = M
                M = M - dist[last][i] + H
                prev_last = last
                last = i
                dfs(D + 1)
                last, M = prev_last, prev_M
                visited[i] = False
visited[0] = True
dfs(0)
print(max_cnt)