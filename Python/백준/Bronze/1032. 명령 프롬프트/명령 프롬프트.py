import sys
N = int(sys.stdin.readline())
inp = sys.stdin.readline().rstrip()
ans = list(inp)
for _ in range(N - 1):
    inp = sys.stdin.readline().rstrip()
    for i in range(len(inp)):
        if ans[i] != inp[i]:
            ans[i] = "?"

print("".join(ans))
