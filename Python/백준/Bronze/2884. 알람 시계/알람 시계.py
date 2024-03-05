import sys
H, M = map(int, sys.stdin.readline().split())
M2 = M + H * 60 - 45
if M2 < 0:
    M2 = 24 * 60 + M2
H2 = M2 // 60
M2 = M2 % 60
print(H2, M2)