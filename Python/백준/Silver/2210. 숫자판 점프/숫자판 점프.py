import sys
inp = []

for _ in range(5):
    inp.append(list(map(int, sys.stdin.readline().split())))

cache = {}
temp = [-1, -1, -1, -1, -1, -1]
tok_x = [1,0,-1,0]
tok_y = [0,1,0,-1]


def dfs(bx, by, x, y, D):
    global temp
    global cache
    if D == 6:
        cache["".join(list(map(str, temp)))] = 1
    else:
        if not (x < 0 or y < 0 or x > 4 or y > 4):
            if not (x == bx and y == by):
                temp[D] = inp[y][x]
                for i in range(4):
                    dfs(x, y, x + tok_x[i], y + tok_y[i], D + 1)
                temp[D] = -1


for i in range(5):
    for j in range(5):
        dfs(-1, -1, i, j, 0)

print(len(cache.keys()))