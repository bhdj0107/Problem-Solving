import sys
l = sys.stdin.readline()
inp = sys.stdin.readline().rstrip()
for i in range(5):
    print(inp[len(inp) - 5 + i], end='')
print()