import sys
from collections import deque

N = int(sys.stdin.readline())
src, dst = map(int, sys.stdin.readline().split())

M = int(sys.stdin.readline())
connection = {i:[] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    connection[a].append(b)
    connection[b].append(a)


dist = [-1 for _ in range(N + 1)]
stack = deque()
stack.append((0, src))

while stack:
    prev, now = stack.pop()
    if (dist[now]) != -1: continue
    else:
        dist[now] = dist[prev] + 1
        for i in connection[now]:
            stack.appendleft((now, i))

print(dist[dst])