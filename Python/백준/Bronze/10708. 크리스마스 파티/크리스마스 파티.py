import sys
N = int(sys.stdin.readline())
G = int(sys.stdin.readline())
target = tuple(map(int, sys.stdin.readline().split()))
score = [0 for _ in range(N)]
for i in range(G):
    inp = tuple(map(int, sys.stdin.readline().split()))
    for j in range(len(inp)):
        if inp[j] == target[i]:
            score[j] += 1
        else:
        	score[target[i]-1] += 1
for i in score:
	print(i)