# 2021 09 27 2150 start
import sys
N, M = map(int, sys.stdin.readline().split())
field = [sys.stdin.readline().rstrip() for _ in range(N)]
ans = -1

def isSquare(N):
    t = N ** 0.5
    return (not bool(t%1))

# 탐색 시작위치 정하기
for y in range(N):
    for x in range(M):
        # 인덱스 증가량 정하기
        for dy in range(-N + 1, N):
            for dx in range(M):
                # Temp 생성
                temp = field[y][x]
                rev_temp = field[y][x]
                if isSquare(int(temp)): ans = max(ans, int(temp))
                if isSquare(int(rev_temp)): ans = max(ans, int(rev_temp))
                if dy == 0 and dx == 0: continue
                tx, ty = x, y # target_x, target_y
                while True:
                    tx += dx
                    ty += dy
                    if tx >= M or ty >= N or tx < 0 or ty < 0: break
                    temp = temp + field[ty][tx]
                    rev_temp = field[ty][tx] + rev_temp
                    if isSquare(int(temp)): ans = max(ans, int(temp))
                    if isSquare(int(rev_temp)): ans = max(ans, int(rev_temp))
print(ans)
                    