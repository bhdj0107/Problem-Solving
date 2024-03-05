import sys
inp = {}
for i in range(9):
    inp[int(sys.stdin.readline())] = i
M = max(inp.keys())
print(M)
print(inp[M] + 1)