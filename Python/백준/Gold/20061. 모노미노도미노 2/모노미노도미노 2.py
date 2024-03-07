import sys
N = int(sys.stdin.readline())
inp = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

score = 0
green = [[0,0,0,0] for _ in range(7)]
blue = [[0,0,0,0] for _ in range(7)]

def drop(block):
    t = block[0]
    y = block[2]
    if t == 1:
        x = 5 - green[6][y]
        green[x][y] = 1
        green[6][y] += 1
    elif t == 2:
        x = 5 - max(green[6][y:y+2])
        green[x][y], green[x][y+1] = 1, 1
        green[6][y], green[6][y+1] = 6-x, 6-x
    elif t == 3:
        x = 5 - green[6][y]
        green[x][y], green[x-1][y] = 1, 1
        green[6][y] += 2
    y = block[1]
    if t == 1:
        x = 5 - blue[6][y]
        blue[x][y] = 1
        blue[6][y] += 1
    elif t == 3:
        x = 5 - max(blue[6][y:y+2])
        blue[x][y], blue[x][y+1] = 1, 1
        blue[6][y], blue[6][y+1] = 6-x, 6-x
    elif t == 2:
        x = 5 - blue[6][y]
        blue[x][y], blue[x-1][y] = 1, 1
        blue[6][y] += 2
              
def line(field):
    global score
    push = [0,0,0,0,0]
    for i in range(5, 1, -1):
        if sum(field[i]) == 4:
            score += 1
            for j in range(i - 1, -1, -1):
                push[j] += 1
    for i in range(4, -1, -1):
        field[i + push[i]] = field[i]
    for i in range(push[0]):
        field[i] = [0,0,0,0]
    for i in range(4):
        field[6][i] = 0
        for j in range(6):
            if field[j][i]:
                field[6][i] = 6 - j
                break

def over(field):
    if sum(field[1]):
        if sum(field[0]):
            delta = 2
        else:
            delta = 1
    else:
        delta = 0
    if delta:
        for i in range(5, 1, -1):
            field[i] = field[i - delta]
        for i in range(4):
            field[6][i] = max(field[6][i] - delta, 0)
        field[0], field[1] = [0,0,0,0],[0,0,0,0]
        
for i in inp:
    drop(i)
    line(green)
    line(blue)
    over(green)
    over(blue)
cnt = 0
for i in (2,3,4,5):
    cnt += sum(green[i]) + sum(blue[i])
print(score)
print(cnt)           