import sys
R, C, T = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
d = ((0, 1), (1, 0), (0, -1), (-1, 0))

for _ in range(T):
    airconPos = []
    newRoom = [[0 for _ in range(C)] for _ in range(R)]
    # 확산
    for i in range(R):
        for j in range(C):
            if room[i][j] == -1: 
                newRoom[i][j] = -1
                airconPos.append((i, j))
                continue
            totalSub = 0
            nextDust = room[i][j] // 5 
            for k in range(4):
                ny, nx = i + d[k][0], j + d[k][1]
                if ny < 0 or ny >= R or nx < 0 or nx >= C: continue
                if room[ny][nx] == -1: continue
                else:
                    newRoom[ny][nx] += nextDust
                    totalSub += nextDust
            newRoom[i][j] += room[i][j] - totalSub
    room = newRoom
    
    # 공청기 아래
    now = airconPos.pop()
    direction = ((0, 1), (1, 0), (0, -1), (-1, 0), (0, 1))
    prev = 0
    stopSignal = True
    for dIdx in range(5):
        while stopSignal:
            ny = now[0] + direction[dIdx][0]
            nx = now[1] + direction[dIdx][1]
            if ny < 0 or ny >= R or nx < 0 or nx >= C: break
            if room[ny][nx] == -1:
                stopSignal = False
                break
            prev, room[ny][nx] = room[ny][nx], prev
            now = (ny, nx)
    
    # 공청기 위
    now = airconPos.pop()
    direction = ((0, 1), (-1, 0), (0, -1), (1, 0), (0, 1))
    prev = 0
    stopSignal = True
    for dIdx in range(5):
        while stopSignal:
            ny = now[0] + direction[dIdx][0]
            nx = now[1] + direction[dIdx][1]
            if ny < 0 or ny >= R or nx < 0 or nx >= C: break
            if room[ny][nx] == -1:
                stopSignal = False
                break
            prev, room[ny][nx] = room[ny][nx], prev
            now = (ny, nx)
            
print(sum([sum(a) for a in room]) + 2)