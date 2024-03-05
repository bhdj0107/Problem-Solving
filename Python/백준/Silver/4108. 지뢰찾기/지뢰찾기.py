import sys
dx = (1, 1, 1, 0, 0, -1, -1, -1)
dy = (0, -1, 1, -1, 1, 0, -1, 1)


def asd():
    while 1:
        R, C = map(int, sys.stdin.readline().split())
    
        if R == 0 and C == 0:
            exit()
        field = [[1 for _ in range(C)] for _ in range(R)]
        for y in range(R):
            inp = sys.stdin.readline().rstrip()
            for x in range(C):
                if inp[x] == '*':
                    field[y][x] *= -1
                    for d in range(8):
                        tx = x + dx[d]
                        ty = y + dy[d]
                        if tx < 0 or ty < 0 or tx >= C or ty >= R:
                            continue
                        field[ty][tx] = field[ty][tx] << 1
    
        for i in field:
            for j in i:
                if j < 0:
                    print("*", end='')
                else:
                    cnt = 0
                    while j != 1:
                        j = j >> 1
                        cnt += 1
                    print(cnt, end='')
            print("")
            
asd()