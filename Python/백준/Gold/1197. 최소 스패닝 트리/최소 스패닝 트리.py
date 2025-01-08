import sys
sys.setrecursionlimit(10**8)
V, E = map(int, sys.stdin.readline().split())

edges = []

for _ in range(E):
    a, b, d = map(int, sys.stdin.readline().split())
    edges.append((a - 1, b - 1, d))
    
edges.sort(key=lambda x : x[2], reverse=True)

roots = [i for i in range(V)]
def getRoot(idx):
    global roots
    if roots[idx] == idx: return idx
    else:
        roots[idx] = getRoot(roots[idx])
        return roots[idx]

total = 0
while edges:
    a, b, d = edges.pop()
    aRoot = getRoot(a)
    bRoot = getRoot(b)
    if aRoot == bRoot: continue
    else:
        if aRoot < bRoot: roots[bRoot] = aRoot
        else: roots[aRoot] = bRoot
        total += d
    
print(total)