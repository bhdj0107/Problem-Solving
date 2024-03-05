import sys
A, B, C = map(int, sys.stdin.readline().split())
time = {}
swap = {1:A, 2:B * 2, 3:C * 3}
for i in range(3):
    ent, ext = map(int, sys.stdin.readline().split())
    for j in range(ent, ext):
        try:
            time[j] += 1
        except:
            time[j] = 1

ans = 0
for i in time.values():
    ans += swap[i]

print(ans)