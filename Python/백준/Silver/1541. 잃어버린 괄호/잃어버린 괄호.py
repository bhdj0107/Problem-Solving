import sys
inp = sys.stdin.readline().rstrip()
inp = list(inp.split("-"))
ans = sum(map(int, inp[0].split("+")))
for i in range(1, len(inp)):
	ans -= sum(map(int, inp[i].split("+")))
print(ans)