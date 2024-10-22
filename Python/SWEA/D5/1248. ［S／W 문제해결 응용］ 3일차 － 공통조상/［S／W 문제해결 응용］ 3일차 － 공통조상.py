import math
T = int(input())
for t in range(1, T + 1):
    V, E, A, B = map(int, input().split())
    MAX_LOG = int(math.log2(V)) + 1
    
    connection = set()
    data = input().split()
    for i in range(E):
        i = i * 2
        a, b = int(data[i]), int(data[i + 1])
        connection.add((a, b))
    
    parent = [[None for _ in range(MAX_LOG)] for _ in range(V + 1)]
    children = [[] for _ in range(V + 1)]
    
    for edge in connection:
        src, dst = edge
        parent[dst][0] = src
        children[src].append(dst)
        
    # update depth
    depth = [-1 for _ in range(V + 1)]
    stack = []
    stack.append((1, 1))
    while stack:
        src, d = stack.pop()
        depth[src] = d
        for child in children[src]:
            stack.append((child, d + 1))
    
    # update (2 ** i) th parent
    for i in range(1, MAX_LOG):
        for j in range(1, V + 1):
            p = parent[j][i - 1]
            if p:
                parent[j][i] = parent[p][i - 1]
    
    
    # FIND LCA A, B
    if depth[B] < depth[A]: A, B = B, A

    # make each depth same
    while True:
        if depth[B] == depth[A]: break
        B = parent[B][0]
    
    # LCA Algorithm
    ret = -1
    if not A == B:
        for i in range(MAX_LOG - 1, -1, -1):
            if parent[A][i] and parent[B][i]:
                if parent[A][i] != parent[B][i]:
                    A = parent[A][i]
                    B = parent[B][i]
        ret = parent[A][0]
    else: ret = A
    
    # count Tree size
    stack = []
    stack.append(ret)
    count = 0
    while stack:
        count += 1
        now = stack.pop()
        for child in children[now]:
            stack.append(child)
    print(f'#{t} {ret} {count}')