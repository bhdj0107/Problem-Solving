import sys
T = int(sys.stdin.readline())

for _ in range(T):
    # N, E, S, W
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    left, top, right, bottom = 0, 0, 0, 0

    nowDirection = 0
    pos = (0, 0)
    ops = sys.stdin.readline().rstrip()
    for op in ops:
        if op == 'L': nowDirection = (nowDirection + 4 - 1) % 4
        elif op == 'R': nowDirection = (nowDirection + 4 + 1) % 4
        else: 
            if op == 'F':
                pos = (pos[0] + directions[nowDirection][0], pos[1] + directions[nowDirection][1])
            elif op == 'B':
                pos = (pos[0] - directions[nowDirection][0], pos[1] - directions[nowDirection][1])
            left = min(left, pos[1])
            right = max(right, pos[1])
            top = min(top, pos[0])
            bottom = max(bottom, pos[0])

    print(abs(left - right) * abs(top - bottom))