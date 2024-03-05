import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # max(M, N) Combination min(M, N)
    if N and M:
        top, bottom = 1, 1
        for i in range(min(M, N)):
            top *= max(M, N) - i
            bottom *= min(N, M) - i
            ans = top // bottom
    else: ans = 0
    print(ans)