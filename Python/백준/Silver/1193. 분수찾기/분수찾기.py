import sys
N = int(sys.stdin.readline()) - 1
cnt = 1
while True:
    if N < cnt:
        break
    else:
        N -= cnt
        cnt += 1
if cnt % 2:
    print(cnt - N, end='')
    print('/', end='')
    print(N + 1)
else:
    print(N + 1, end='')
    print('/', end='')
    print(cnt - N)