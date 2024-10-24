import sys
input = sys.stdin.readline
from collections import deque
d = ((-1, 0), (0, -1), (1, 0), (0, 1))

class Shark:
    def __init__(self, pos):
        self.pos = pos
        self.size = 2
        self.eatCount = 0
    
    def eatFish(self, field, pos):
        y, x = pos
        field[y][x] = 0
        
        self.pos = pos
        self.eatCount += 1
        if self.eatCount == self.size:
            self.eatCount = 0
            self.size += 1
    
    def findClosestFish(self, field):
        q = deque()
        q.append(((self.pos), 0))
        visited = set()
        fish, distance = None, 2147483647
        while q:
            now, dist = q.popleft()
            if now in visited: continue
            visited.add(now)
            if dist > distance: continue
            
            if field[now[0]][now[1]] != 0:
                if field[now[0]][now[1]] < self.size:
                    if fish:
                        if fish[0] > now[0]: fish = now
                        elif fish[0] == now[0]:
                            if fish[1] > now[1]: fish = now
                    else: fish, distance = now, dist
                elif field[now[0]][now[1]] == self.size:
                    for i in range(4):
                        ny, nx = now[0] + d[i][0], now[1] + d[i][1]
                        if self.isPosInField(field, (ny, nx)): 
                            q.append(((ny, nx), dist + 1))
                    
            else:
                for i in range(4):
                    ny, nx = now[0] + d[i][0], now[1] + d[i][1]
                    if self.isPosInField(field, (ny, nx)): 
                        q.append(((ny, nx), dist + 1))
        
        return (fish, distance)
    
    def isPosInField(self, field, pos):
        N = len(field)
        if pos[0] < 0 or pos[0] >= N or pos[1] < 0 or pos[1] >= N: return False
        else: return True
        
T = 1
for t in range(T):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if field[i][j] == 9:
                shark = Shark((i, j))
                field[i][j] = 0
    
    total = 0
    
    while True:
        fish, dist = shark.findClosestFish(field)
        if not fish: break
        else:
            shark.eatFish(field, fish)
            total += dist
     
    print(f'{total}')