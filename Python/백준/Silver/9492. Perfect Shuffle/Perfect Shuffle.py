import sys
from collections import deque
N = 1
while N:
    N = int(sys.stdin.readline())
    temp = [deque(), deque()]
    swap = {0:1, 1:0}
    tok = 0
    for _ in range(N // 2 + N % 2):
        temp[0].append(sys.stdin.readline().rstrip())
    for _ in range(N // 2):
        temp[1].append(sys.stdin.readline().rstrip())
    for _ in range(N):
        print(temp[tok].popleft())
        tok = swap[tok]
        
        
        