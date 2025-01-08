import sys
from collections import deque

d = ((0, 1), (0, -1), (-1, 0), (1, 0))
class Field:
    def __init__(self):
        self.field = None
        self.balls = {}
        
    def copyFromField(self, f):
        field = f.field
        self.field = [[field[i][j] for j in range(len(field[i]))] for i in range(len(field))]

        balls = f.balls
        self.balls = {}
        self.balls['R'] = tuple(list(balls['R'][:-1]) + [False])
        self.balls['B'] = tuple(list(balls['B'][:-1]) + [False])

    def calculateBalls(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j] == 'R':
                    self.balls['R'] = (i, j, 'R', False, False)
                elif self.field[i][j] == 'B':
                    self.balls['B'] = (i, j, 'B', False, False)
                    
    def tilt(self, direction):
        newField = Field()
        newField.copyFromField(self)
        
        a = 1234
        # 우, 좌, 상, 하 [0, 1, 2, 3]
        # 오른쪽 방향일 때
        if direction == 0:
            first, last = list(sorted(list(newField.balls.values()), key=lambda x : -x[1]))
        # 왼쪽 방향일 때
        elif direction == 1:
            first, last = list(sorted(list(newField.balls.values()), key=lambda x : x[1]))
        # 위쪽 방향일 때
        elif direction == 2:
            first, last = list(sorted(list(newField.balls.values()), key=lambda x : x[0]))
        # 오른쪽 방향일 때
        elif direction == 3:
            first, last = list(sorted(list(newField.balls.values()), key=lambda x : -x[0]))

        newField.moveBall(first[2], direction, isFirst=True)
        newField.moveBall(last[2], direction, isFirst=False)
        
        return newField
            
    def moveBall(self, color, direction, isFirst):
        y, x, color, isOut, didntMove = self.balls[color]
        while True:
            ny, nx = y + d[direction][0], x + d[direction][1]
            if self.field[ny][nx] == '#': break
            elif self.field[ny][nx] == 'O':
                isOut = True
                y, x = (-1, -1)
                break
            elif not isFirst and self.field[ny][nx] != '.': break
            else: y, x = ny, nx
        
        origin = self.balls[color]
        if origin[:2] == (y, x):
            didntMove = True
        else:
            self.field[origin[0]][origin[1]] = '.'
            if y != -1: self.field[y][x] = color
        
        self.balls[color] = (y, x, color, isOut, didntMove)
        
N, M = map(int, sys.stdin.readline().split())
field = [sys.stdin.readline().rstrip() for _ in range(N)]

rootField = Field()
rootField.field = field
rootField.calculateBalls()

q = deque()
q.append((rootField, 0))

answer = -1
while q:
    nowField, count = q.popleft()
    if count == 10: break
    for i in range(4):
        newField = nowField.tilt(i)
        if newField.balls['B'][3] or (newField.balls['B'][4] and newField.balls['R'][4]): continue
        else:
            if newField.balls['R'][3]:
                answer = count + 1
                break
            else:
                q.append((newField, count + 1))
    if answer != -1: break
print(answer)