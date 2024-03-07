import sys
sys.setrecursionlimit(10**8)
def a():
    N, M = map(int, sys.stdin.readline().split())
    chk = {i : False for i in range(N)}
    output = [0 for _ in range(8)]
    def dfs(D):
        if D == 0:
            for i in output[:M - 1]:
                print(i, end=" ")
            print(output[:M][-1])
        else:
            for i in range(N):
                if chk[i] == True:
                    continue
                else:
                    chk[i] = True
                    output[M - D] = i + 1
                    dfs(D - 1)
                    output[M - D] = 0
                    chk[i] = False

    dfs(M)    
a()