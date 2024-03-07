import sys
N = int(sys.stdin.readline())
cnt = 0
i = 1
if N == 1:
    print(0)
    exit()
while i*2 < N:
    cnt += i
    i = i*2

print(cnt + int((N+1)/2))
