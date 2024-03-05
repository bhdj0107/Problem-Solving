import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    N = N - 1
    num = N // H
    floor = N - num * H 
    print((floor + 1) * 100 + num + 1)