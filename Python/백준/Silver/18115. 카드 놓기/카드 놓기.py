import sys
from collections import deque
N = int(sys.stdin.readline())
dq = deque() 
inp = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    if inp[-1 * (i + 1)] == 1:
        dq.append(i + 1)
    elif inp[-1 * (i + 1)] == 2:
        tmp = dq.pop()
        dq.append(i + 1)
        dq.append(tmp)
    else:
        dq.appendleft(i + 1)
for _ in range(N - 1):
    print(dq.pop(), end=' ')
print(dq.pop())
