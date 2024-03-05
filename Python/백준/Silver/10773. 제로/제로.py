import sys
def a():
    N = int(sys.stdin.readline())
    inp = []
    for _ in range(N):
        tmp = int(sys.stdin.readline())
        if tmp == 0:
            inp.pop()
        else:
            inp.append(tmp)
    print(sum(inp))
a()