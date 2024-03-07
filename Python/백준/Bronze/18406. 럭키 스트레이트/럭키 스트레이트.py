import sys
inp = sys.stdin.readline().rstrip()
A = 0
B = 0

for i in range(len(inp) // 2):
    A += int(inp[0 + i])
    B += int(inp[len(inp) // 2 + i])

if A == B:
    print("LUCKY")
else:
    print("READY")