import sys
T = int(sys.stdin.readline())
def ans(m, n):
    field = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    count = 0
    for j in range(n):
        b = 0
        h = 0
        for i in range(m):
            if field[i][j] == 1:
                b += 1
                h += m - i
        count += h - (b*(b+1)//2)
    # while queue:
    #     i, j = queue.pop()
    #     tc = 0
    #     for k in range(i + 1, m):
    #         if field[k][j] == 0:
    #             tc += 1
    #         else:
    #             break
    #     field[i][j], field[i + tc][j] = 0, 1
    #     count += tc
    print(count)
for _ in range(T):
    ans(*map(int, sys.stdin.readline().split()))