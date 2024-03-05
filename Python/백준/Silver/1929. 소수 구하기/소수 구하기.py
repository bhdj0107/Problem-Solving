import sys
M, N = map(int, sys.stdin.readline().split())
table = {i:1 for i in range(2, N + 1)}
table[1]=0
for i in range(2, N//2+1):
    if table[i]:
    	for j in range(2, N//i+1):
    		table[i*j]=0
for i in range(M, N+1):
	if table[i]:
		print(i)