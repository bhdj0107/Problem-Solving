import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    X = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    if X[0] == '':
        X = deque()
    else:
        X = deque(map(int, X))
    
    idx = 0
    er = False
    for i in p:
        if i == 'R':
            idx = (idx + 1) % 2
        else:
            if len(X):
                if idx:
                    X.pop()
                else:
                    X.popleft()
            else:
                er = True
                break
    if er:
        print('error')
    else:
        if len(X) == 0:
            print('[]')
        else:
            if idx:
                print('[', end='')
                while len(X) - 1:
                    print(X.pop(), end=',')
                print(X.pop(), end=']\n')
            else:
                print('[', end='')
                while len(X) - 1:
                    print(X.popleft(), end=',')
                print(X.pop(), end=']\n')