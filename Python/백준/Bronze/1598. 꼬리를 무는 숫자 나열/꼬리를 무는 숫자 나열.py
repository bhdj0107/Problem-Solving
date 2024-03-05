import sys
N, M = map(int, sys.stdin.readline().split())
N, M = N - 1, M - 1
Nx, Ny = N // 4, N % 4
Mx, My = M // 4, M % 4
print(abs(Mx - Nx) + abs(My - Ny))