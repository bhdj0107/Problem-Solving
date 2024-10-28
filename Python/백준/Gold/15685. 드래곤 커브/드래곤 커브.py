import sys

N = int(sys.stdin.readline())
curves = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# direction
# 0 -> +X
# 1 -> -Y
# 2 -> -X
# 3 -> +Y

points = set()

d = ((0, 1), (-1, 0), (0, -1), (1, 0))
for curve in curves:
    x, y, direction, gen = curve
    lines = [direction]
    for _ in range(gen):
        newLine = []
        for line in lines:
            # 시계방향으로 돌리고 뒤집기
            line = (line + 1) % 4
            newLine.append(line)
            
        for line in newLine[::-1]:
            lines.append(line)
    now = [y, x]
    points.add(tuple(now))
    for line in lines:
        line = d[line]
        now[0] += line[0]
        now[1] += line[1]
        points.add(tuple(now))

d = ((0, 1), (1, 0), (1, 1))
cnt = 0
for p in points:
    flag = True
    for dd in d:
        dy, dx = dd
        pp = (p[0] + dy, p[1] + dx)
        if pp not in points: 
            flag = False
            break
    if flag: cnt += 1

print(cnt) 