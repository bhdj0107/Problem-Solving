import sys
A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())
N = sys.stdin.readline().rstrip()
cnt = 0
A = 100 * A + B
C = 100 * C + D
for i in range(A, C + 1):
    if i % 100 > 59: continue
    if i < 1000: t = "0" + str(i)
    else: t = str(i)
    if str(N) in t:
        cnt += 1
print(cnt)
