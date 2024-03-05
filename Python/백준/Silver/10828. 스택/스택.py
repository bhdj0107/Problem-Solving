import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    inp = (sys.stdin.readline() +" 0").split()
    if inp[0] == "push":
        queue.append(int(inp[1]))
    elif inp[0] == "pop":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif inp[0] == "size":
        print(len(queue))
    elif inp[0] == "empty":
        print(int(not(len(queue))))
    elif inp[0] == "top":
        if not queue:
            print("-1")
        else:
            temp = queue.pop()
            print(temp)
            queue.append(temp)