import sys
N = int(sys.stdin.readline())
M = 0
ans = []
for i in range(N):
    inp = list(sys.stdin.readline().split())
    if M < int(inp[1]):
        ans = [inp[0]]
        M = int(inp[1])
    elif M == int(inp[1]):
        ans.append(inp[0])
    else:
        continue
ans.sort()
print(ans[0])