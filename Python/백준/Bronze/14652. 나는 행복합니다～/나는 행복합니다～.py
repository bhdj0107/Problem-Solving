# 2020 07 02 1853 start
import sys
N, M, K = map(int, sys.stdin.readline().split())
print(K // M, K % M)