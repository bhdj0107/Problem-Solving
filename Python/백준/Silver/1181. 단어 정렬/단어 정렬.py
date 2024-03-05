import sys
def a():
    N = int(sys.stdin.readline())
    temp = {}
    for _ in range(N):
        S = sys.stdin.readline().rstrip()
        if len(S) in temp:
            temp[len(S)].add(S)
        else:
            
            temp[len(S)] = set((S,))
            
    for i in sorted(temp.keys()):
        for j in sorted(list(temp[i])):
            print(j)
a()