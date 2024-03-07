import sys
N, H, W = map(int, sys.stdin.readline().split())
inp = []
for _ in range(H):
    inp.append(sys.stdin.readline().rstrip())

for i in range(N):
    C = '?'
    for j in range(H * W):
        x, y = j % W + W * i, j // W
        if inp[y][x] != '?':
            C = inp[y][x]
            break
    print(C, end='')
