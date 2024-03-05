import sys
def a():
    T = int(sys.stdin.readline())
    for i in range(T):
        print("Case " + str(i + 1)+":")
        N = int(sys.stdin.readline())
        for _ in range(N):
            n = int(sys.stdin.readline())
            if n != 6:
                print(n + 1)
a()