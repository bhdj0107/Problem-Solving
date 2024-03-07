import sys
def a():
    N, M = map(int, sys.stdin.readline().split())
    A = []
    for _ in range(N):
    	A.append(list(map(int, sys.stdin.readline().split())))
    m = tuple(map(int, sys.stdin.readline().split()))
    Move = []
    for _ in range(M - 1):
    	Move.append(tuple(map(int, sys.stdin.readline().split())))
    
    
    direction = ((0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
    dy = direction[m[0]][0] * m[1]
    dx = direction[m[0]][1] * m[1]
    cloud = set([((2 * N - 1 + dy) % N, (N + dx) % N), ((2 * N - 1 + dy) % N, (N + dx + 1) % N), ((2 * N - 2 + dy) % N, (N + dx) % N), ((2 * N - 2 + dy) % N, (N + dx + 1) % N)])
    
    
    for i in Move:
    	for j in cloud:
    		y, x = j
    		A[y][x] += 1
    		for mx in (-1, 1):
    			for my in (-1, 1):
    				if 0 <= x + mx < N and 0 <= y + my < N:
    					A[y][x] += int((y + my, x + mx) in cloud or A[y + my][x + mx] > 0)
    	tmp = set()
    	dy = direction[i[0]][0] * i[1]
    	dx = direction[i[0]][1] * i[1]
    	for cx in range(N):
    		for cy in range(N):
    			if (cy, cx) in cloud:continue
    			if A[cy][cx] >= 2:
    				A[cy][cx] -= 2
    				tmp.add(((cy + N + dy) % N, (cx + N + dx) % N))
    	cloud = tmp
    
    for j in cloud:
    	y, x = j
    	A[y][x] += 1
    	for mx in (-1, 1):
    		for my in (-1, 1):
    			if 0 <= x + mx < N and 0 <= y + my < N:
    				A[y][x] += int((y + my, x + mx) in cloud or A[y + my][x + mx] > 0)
    for cx in range(N):
    	for cy in range(N):
    		if (cy, cx) in cloud:continue
    		if A[cy][cx] >= 2:
    			A[cy][cx] -= 2
    
    ans = 0
    for a in A:
    	ans += sum(a)
    print(ans)
a()