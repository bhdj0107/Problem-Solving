import sys
T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    ans = [-1, 24 * 60 + 59]
    cnt = 0
    student = set(map(int,sys.stdin.readline().split()))
    N = int(sys.stdin.readline())
    for _ in range(N):
        num, hour, minute = map(int,sys.stdin.readline().split())
        if num in student and hour != -1 and minute != -1:
            if (hour == 6 and minute == 0) or hour < 6:
                cnt = cnt + 1
                if ans[1] > hour * 60 + minute:
                    ans[0], ans[1] = num, hour * 60 + minute
    print(ans[0], cnt)