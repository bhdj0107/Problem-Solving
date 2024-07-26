import sys
R, C, N = map(int, sys.stdin.readline().split())
field = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

class Map:
    def __init__(self, field):
        self.N = len(field)
        self.M = len(field[0])

        self.field = [[[False, 0] for _ in range(self.M)] for _ in range(self.N)]
        self.time = 0

        bombPts = []
        for i in range(self.N):
            for j in range(self.M):
                if field[i][j] == 'O':
                    bombPts.append((i, j))
        
        self.setBomb(bombPts)
        
    def setBomb(self, pts):
        for pt in pts:
            y, x = pt
            self.field[y][x] = [True, self.time]

    def explodeBomb(self, pts):
        d = ((-1, 0), (0, 1), (1, 0), (0, -1))
        for pt in pts:
            y, x = pt
            self.field[y][x][0] = False
            for i in range(4):
                ny, nx = y + d[i][0], x + d[i][1]
                if ny >= 0 and ny < self.N and nx >= 0 and nx < self.M:
                    self.field[ny][nx][0] = False
    
    def fillEmptyCell2Bomb(self):
        emptyPts = []
        for i in range(self.N):
            for j in range(self.M):
                if not self.field[i][j][0]:
                    emptyPts.append((i, j))
        self.setBomb(emptyPts)
    
    def tickTime(self):
        self.time += 1

    def explode3cntBefore(self):
        bombPts = []
        for i in range(self.N):
            for j in range(self.M):
                if self.field[i][j][0] and self.field[i][j][1] - self.time <= -2:
                    bombPts.append((i, j))
        self.explodeBomb(bombPts)

    def printField(self):
        for i in range(self.N):
            for j in range(self.M):
                print('O' if self.field[i][j][0] else '.', end='')
            print()

newMap = Map(field)
newMap.tickTime()
while True:
    if newMap.time >= N: break
    newMap.fillEmptyCell2Bomb()
    newMap.tickTime()

    if newMap.time >= N: break
    newMap.explode3cntBefore()
    newMap.tickTime()

newMap.printField()