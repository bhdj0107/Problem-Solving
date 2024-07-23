import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())
connection = {i:[] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    connection[a].append(b)
    connection[b].append(a)

for i in range(1, N + 1):
    connection[i].sort()

visited = [False for _ in range(N + 1)]
stack = deque()
stack.append(V)

order = []
while stack:
    now = stack.pop()
    if (visited[now]): continue
    else:
        order.append(str(now))
        visited[now] = True
        for i in reversed(connection[now]):
            stack.append(i)

print(" ".join(order))

visited = [False for _ in range(N + 1)]
stack = deque()
stack.append(V)

order = []
while stack:
    now = stack.pop()
    if (visited[now]): continue
    else:
        order.append(str(now))
        visited[now] = True
        for i in connection[now]:
            stack.appendleft(i)
            
print(" ".join(order))