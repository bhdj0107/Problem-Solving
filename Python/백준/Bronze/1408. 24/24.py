import sys
t_now = tuple(map(int, sys.stdin.readline().split(":")))
t_start = tuple(map(int, sys.stdin.readline().split(":")))

t_now = 3600 * t_now[0] + 60 * t_now[1] + t_now[2]
t_start = 3600 * t_start[0] + 60 * t_start[1] + t_start[2]

t = t_now - t_start
if t < 0:
    t = -t
    ans = [0,0,0]
    ans[0] = str(t // 3600)
    t = t % 3600
    ans[1] = str(t // 60)
    t = t % 60
    ans[2] = str(t)
else:
    t = 86400 - t
    ans = [0,0,0]
    ans[0] = str(t // 3600)
    t = t % 3600
    ans[1] = str(t // 60)
    t = t % 60
    ans[2] = str(t)
    
for i in range(3):
    if len(ans[i]) == 1:
        ans[i] = "0" + ans[i]
print(ans[0] + ":" + ans[1] + ":" + ans[2])