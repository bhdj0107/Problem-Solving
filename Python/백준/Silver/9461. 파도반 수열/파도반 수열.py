import sys
dp = [[0 for _ in range(50)] for _ in range(2)]

dp[0][0] = 1
dp[1][0] = 1
dp[0][1] = 1
dp[1][1] = 2

for i in range(2, 50):
    dp[0][i] = dp[0][i - 1] + dp[1][i - 2]
    dp[1][i] = dp[0][i - 1] + dp[1][i - 1]

N = int(sys.stdin.readline())
for _ in range(N):
    a = int(sys.stdin.readline()) - 1
    isUpper = a % 2
    idx = a // 2
    print(dp[isUpper][idx])