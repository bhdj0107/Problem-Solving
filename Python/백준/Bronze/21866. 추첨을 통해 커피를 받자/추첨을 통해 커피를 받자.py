import sys
inp = list(map(int, sys.stdin.readline().split()))
max_score = (100, 100, 200, 200, 300, 300, 400, 400, 500)
ans = None
for i in range(len(inp)):
    if inp[i] > max_score[i]:
        ans = "hacker"
        break
if ans == None:
    if sum(inp) >= 100: ans = "draw"
    else: ans = "none"
print(ans)