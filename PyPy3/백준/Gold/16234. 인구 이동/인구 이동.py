import sys
input = sys.stdin.readline
from collections import defaultdict, deque
N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]
d = ((0, 1), (1, 0), (-1, 0), (0, -1))
class World:
    def __init__(self, countries, L, R):
        self.countries = countries
        self.N = len(countries)
        self.L = L
        self.R = R
        self.barrierStatus = defaultdict(set)
    
    def movePopulation(self):
        countries = []
        visited = set()
        
        for i in range(self.N):
            for j in range(self.N):
                if (i, j) in visited: continue
                else:
                    q = deque()
                    connected = []
                    q.append((i, j))
                    while q:
                        now = q.popleft()
                        if now in visited: continue
                        visited.add(now)
                        connected.append(now)
                        for k in range(4):
                            ny, nx = now[0] + d[k][0], now[1] + d[k][1]
                            if 0 <= ny < N and 0 <= nx < N: 
                                if (ny, nx) in self.barrierStatus[now]:
                                    q.append((ny, nx))
                                    
                    if len(connected) > 1: countries.append(connected)
        for block in countries:
            total = 0
            for country in block: total += self.countries[country[0]][country[1]]
            total //= len(block)
            for country in block: self.countries[country[0]][country[1]] = total
                             
        
    def resetBarrier(self):
        self.barrierStatus = defaultdict(set)
        for i in range(self.N):
            for j in range(self.N):
                self.openBarrier((i, j))
    
        
    def openBarrier(self, src):
        for i in range(2, 4):
            neighbor = src[0] + d[i][0], src[1] + d[i][1]
            if not (0 <= neighbor[0] < self.N and 0 <= neighbor[1] < self.N): continue
            if self.isBarrierCanOpen(src, neighbor):
                self.barrierStatus[src].add(neighbor)
                self.barrierStatus[neighbor].add(src)

        
    def isBarrierCanOpen(self, src, dst):
        diff = abs(self.countries[src[0]][src[1]] - self.countries[dst[0]][dst[1]])
        if self.L <= diff <= self.R: return True
        else: return False

cnt = 0
world = World(countries, L, R)
while True:
    world.resetBarrier()
    if len(world.barrierStatus):
        cnt += 1
        world.movePopulation()
    else: break
print(cnt)