import sys
from collections import deque as dq
N = int(sys.stdin.readline())
deque = dq()
for i in range(1, N + 1):
    deque.append(i)
while len(deque) > 1:
    deque.popleft()
    deque.append(deque.popleft())
print(deque.pop())