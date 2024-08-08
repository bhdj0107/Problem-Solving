import sys
N, M = map(int, sys.stdin.readline().split())
R, C, D = map(int, sys.stdin.readline().split())
room = [list(sys.stdin.readline().split()) for _ in range(N)]

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.

# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    # 3. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    # 3-1. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
    
# 4. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    # 5. 반시계 방향으로 90도 회전한다.
    # 6. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    # 7. 1번으로 돌아간다.

visited = [[False for _ in range(M)] for _ in range(N)]
cnt = 0
while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if not visited[R][C]:
        visited[R][C] = True
        cnt += 1

    # 주변칸의 청소 여부 확인
    unCleanedCell = False
    for d in range(4):
        nr = R + directions[d][0]
        nc = C + directions[d][1]
        if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
        if room[nr][nc] == '1': continue
        if not visited[nr][nc]:
            unCleanedCell = True
            break
    
    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    if not unCleanedCell:
        # 후방의 벽 여부
        nr = R - directions[D][0]
        nc = C - directions[D][1]
        isPosInRoom = (nr >= 0 and nr < N and nc >= 0 and nc < M)
        if isPosInRoom: isBackIsWall = room[nr][nc] == '1'
        else: isBackIsWall = False
        
        # 3. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        if not isBackIsWall:
            R, C = nr, nc
        
        # 3-1. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else: break
        
    # 4. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    else:
        # 5. 반시계 방향으로 90도 회전한다.
        D = (D + 3) % 4
        
        # 전방의 청소 여부
        nr = R + directions[D][0]
        nc = C + directions[D][1]
        isPosInRoom = (nr >= 0 and nr < N and nc >= 0 and nc < M)
        if isPosInRoom: isFrontNotClean = room[nr][nc] == '0' and not visited[nr][nc]
        else: isFrontNotClean = False
        
        # 6. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        if isFrontNotClean:
            R, C = nr, nc
            
        # 7. 1번으로 돌아간다.
        
print(cnt)