import sys
from collections import deque

N, T = map(int, sys.stdin.readline().split())
connection = []
for _ in range(N):
    connection.append(int(sys.stdin.readline()))

dist = [-1 for _ in range(N)]
q = deque()
q.append((0, 0))

while q:
    prev, now = q.popleft()
    if dist[now] != -1: continue
    dist[now] = dist[prev] + 1
    q.append((now, connection[now]))

print(dist[T])