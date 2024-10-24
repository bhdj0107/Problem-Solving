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
        self.barrierHash = {}
    
    def movePopulation(self):
        visited = set()
        isSwapped = False
        
        for i in range(self.N):
            for j in range(self.N):
                if (i, j) in visited: continue
                else:
                    q = deque()
                    total = 0
                    connected = []
                    q.append((i, j))
                    while q:
                        now = q.popleft()
                        if now in visited: continue
                        visited.add(now)
                        connected.append(now)
                        total += self.countries[now[0]][now[1]]
                        for k in range(4):
                            ny, nx = now[0] + d[k][0], now[1] + d[k][1]
                            if 0 <= ny < N and 0 <= nx < N: 
                                if self.isBarrierCanOpen(now, (ny, nx)):
                                    q.append((ny, nx))
                                    
                    if len(connected) > 1:
                        isSwapped = True
                        total = total // len(connected)
                        for country in connected: self.countries[country[0]][country[1]] = total
                        
        self.barrierHash = {}
        return isSwapped
    
    def isBarrierCanOpen(self, src, dst):
        if self.barrierHash.get((src, dst)): return self.barrierHash.get((src, dst))
        
        diff = abs(self.countries[src[0]][src[1]] - self.countries[dst[0]][dst[1]])
        ret = self.L <= diff <= self.R
        self.barrierHash[(src, dst)] = ret
        self.barrierHash[(dst, src)] = ret
        
        return ret
        

cnt = 0
world = World(countries, L, R)
while True:
    if not world.movePopulation(): break
    cnt += 1
print(cnt)