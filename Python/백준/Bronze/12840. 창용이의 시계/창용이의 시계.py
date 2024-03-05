import sys
#a_day_to_sec = 86400

H, M, S = map(int, sys.stdin.readline().split())

now = H * 60 * 60 + M  * 60 + S

tc = int(sys.stdin.readline())
for _ in range(tc):
	inp = sys.stdin.readline().split()
	T = int(inp[0])
	try:
		c = int(inp[1])
	except:
		None
	if T == 1:
		now = (now + c) % 86400
	elif T == 2:
		now = (86400 + now - c) % 86400
	else:
		print(now // 3600, now // 60 - (now // 3600 * 60), now % 60)