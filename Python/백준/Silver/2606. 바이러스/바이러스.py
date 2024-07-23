from collections import deque
import sys

def asd():
    N = int(sys.stdin.readline())
    chk = set()
    chk.add(1)

    pair = {i: set() for i in range(1, N + 1)}

    M = int(sys.stdin.readline())

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        pair[a].add(b)
        pair[b].add(a)

    chk.update(pair[1])
    queue = deque(pair[1])
    while queue:
        temp = queue.popleft()
        queue.extend(pair[temp] - chk)
        chk.update(pair[temp])
    print(len(chk) - 1)

asd()