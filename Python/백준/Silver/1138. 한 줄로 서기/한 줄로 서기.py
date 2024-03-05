import sys
N = int(sys.stdin.readline())
inp = tuple(map(int, sys.stdin.readline().split()))
ans = [0 for _ in range(N)]
cnt_zero = [i for i in range(N)]
for i in range(N):
    tmp = False
    for j in range(N):
        if tmp:
            cnt_zero[j] -= 1
        else:
            if inp[i] == cnt_zero[j]:
                tmp = True
                ans[j] = i + 1
                cnt_zero[j] = -1
for i in ans[:-1]:
    print(i, end=" ")
print(ans[-1])