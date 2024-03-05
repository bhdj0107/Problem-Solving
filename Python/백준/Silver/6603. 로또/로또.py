from collections import deque
import sys
limit = 6
temp = deque()

def dfs(D):
    global temp
    if len(temp) == limit:
        for i in range(5):
            print(S[temp[i]], end=" ")
        print(S[temp[5]])
    else:
        for i in range(D + 1, S[0] + 1):
            temp.append(i)
            dfs(i)
            temp.pop()



while 1:
    S = list(map(int, sys.stdin.readline().split()))
    if S[0] == 0:
        break
    dfs(0)
    print("")