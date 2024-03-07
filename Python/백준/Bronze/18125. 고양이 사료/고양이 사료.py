import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
q_pic = deque()
for _ in range(R):
    q_pic.append(deque())

for i in range(C):
    temp = tuple(map(int, sys.stdin.readline().split()))
    for j in range(R):
        q_pic[j].appendleft(temp[j])

q_ans = deque()
for i in range(R):
    q_ans.append(deque(map(int, sys.stdin.readline().split())))


if q_ans == q_pic:
    print('''|>___/|        /}
| O < |       / }
(==0==)------/ }
| ^  _____    |
|_|_/     ||__|''')
else:
    print('''|>___/|     /}
| O O |    / }
( =0= )""""  \\
| ^  ____    |
|_|_/    ||__|''')