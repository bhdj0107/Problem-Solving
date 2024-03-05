import sys
N = int(sys.stdin.readline())
cnt = 0  
for i in range((N - 4) // 2 + 1):
    cnt = cnt + i

print(cnt)