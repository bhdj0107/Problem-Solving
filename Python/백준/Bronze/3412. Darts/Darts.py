import sys
def a():
    T = int(sys.stdin.readline())
    for _ in range(T):
        ans = 0
        N = int(sys.stdin.readline())
        for _ in range(N):
            x, y = map(int, sys.stdin.readline().split())
            for i in range(1,11):
                if x * x + y * y <= 400 * i * i:
                    ans += 11 - i
                    break
        print(ans)
a()