import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
connection = {i:[] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    connection[a].append(b)
    connection[b].append(a)


visited = [False for _ in range(N + 1)]
stack = deque()
stack.append(1)

cnt = 0
while stack:
    now = stack.pop()
    if (visited[now]): continue
    else:
        cnt += 1
        visited[now] = True
        for i in connection[now]:
            stack.append(i)

print(cnt - 1)