import sys
while True:
    inp = tuple(map(int, sys.stdin.readline().split()))
    if inp == (0,):
        exit()
    cnt = 1
    for i in range(inp[0]):
        cnt *= inp[2 * i + 1]
        cnt -= inp[2 * (i+1)]
    print(cnt)

