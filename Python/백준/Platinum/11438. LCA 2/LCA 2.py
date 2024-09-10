import sys
sys.setrecursionlimit(10**8)
N = int(sys.stdin.readline())
class Graph:
    def __init__(self, N):
        self.connections = [
            set() for _ in range(N + 1)
        ]
        
        self.depth = [-1 for _ in range(N + 1)]
        self.parents = [[-1 for _ in range(18)] for _ in range(N + 1)]
        
    def addConnection(self, a, b):
        self.connections[a].add(b)
        self.connections[b].add(a)
    
    def updateDepth(self):
        visited = [False for _ in range(N + 1)]
        visited[1] = True
        self.dfs(0, 1, visited)
        
    def dfs(self, D, now, visited):
        self.depth[now] = D
        for nextNode in self.connections[now]:
            if visited[nextNode]: continue
            self.parents[nextNode][0] = now
            visited[nextNode] = True
            self.dfs(D + 1, nextNode, visited)
    
    def setParent(self):
        for j in range(1, 18):
            for i in range(1, N + 1):
                p = self.parents[i][j - 1]
                if p == -1: continue
                self.parents[i][j] = self.parents[p][j - 1]
                
    def LCA(self, a, b):
        # a 가 더 깊도록 보정
        if self.depth[a] < self.depth[b]: a, b = b, a
        
        # 두 노드의 깊이가 같도록 a에서 거슬러 올라감
        for i in range(18, -1, -1):
            if self.parents[b] == -1: continue
            # a의 현재 깊이 - 거슬러 올라갈 높이 >= b의 현재 깊이인 경우 swap
            if self.depth[a] - (2 ** i) >= self.depth[b]:
                a = self.parents[a][i]
        
        if a == b: return a
        
        # 거슬러 올라가기
        for i in range(17, -1, -1):
            if self.parents[a][i] != self.parents[b][i]:
                a = self.parents[a][i]
                b = self.parents[b][i]
        
        return self.parents[a][0]
    
graph = Graph(N)
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph.addConnection(a, b)
M = int(sys.stdin.readline())
pairs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

graph.updateDepth()
graph.setParent()

for a, b in pairs:
    print(graph.LCA(a, b))