import sys
front, back = list(sys.stdin.readline().rstrip()[:]), []
N = int(sys.stdin.readline())
for _ in range(N):
	inp = sys.stdin.readline().rstrip()
	if inp == 'L':
		if front:
			back.append(front.pop())
	elif inp == 'D':
		if back:
			front.append(back.pop())
	elif inp == 'B':
		if front:
			front.pop()
	else:
		front.append(inp[-1])
while back:
	front.append(back.pop())
print("".join(front))