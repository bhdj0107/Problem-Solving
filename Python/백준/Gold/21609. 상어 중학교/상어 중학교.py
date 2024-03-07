# 2021 06 06 1510 start
import sys
from collections import deque as dq
N, M = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

score = 0
direction = 0
group = []
def grouping():
    # 좌측 상단부터 각각의 칸에 그룹을 미리 계산 해놓는 함수
    global group
    group = []
    
    # 각 칸이 어느 그룹에 속하는지 저장할 배열
    where = [[-1 for _ in range(N)] for _ in range(N)]
    
    # 좌측 상단부터 처리를 시작
    for i in range(N):
        for j in range(N):
            # 해당 칸이 일반 색인데, 아직 그룹이 확정지어지지 않은 경우 
            if where[i][j] == -1 and 0 < field[i][j]:
                # 먼저 새로운 빈 그룹을 group 리스트에 추가
                group.append([])
                
                # 이후 해당좌표에서 BFS를 수행한다
                queue = dq()
                queue.append((i,j))
                group_num = len(group) - 1
                group_val = field[i][j]
                while queue:
                    tmp = queue.popleft()
                    x, y = tmp[0], tmp[1]
                    # 만약 큐에서 꺼내온 좌표가 그룹 미정이거나, 현재 그룹에 포함되지 않은 0일 경우
                    if where[x][y] == -1 or (field[x][y] == 0 and where[x][y] != group_num):
                        # 해당 좌표를 새로운 그룹에 추가한다.
                        group[-1].append((x,y))
                        # 그리고 좌표의 그룹값을 수정한다.
                        where[x][y] = group_num
                        
                        # 이후 상하좌우를 현재칸과 비교한다.
                        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                            # x+dx, y+dy 과 0 이상 N 미만일 경우에만
                            if 0 <= x + dx < N and 0 <= y + dy < N:
                                # 비교칸과 그룹색을 비교하여, 같거나 또는 비교칸이 0인 경우에만 큐에 집어넣는다
                                if group_val == field[x+dx][y+dy] or field[x+dx][y+dy] == 0:
                                    queue.append((x+dx, y+dy))

def delete_block():
    global score, field
    
    # 가장 큰 그룹을 기억할 변수 index
    index = (-1, -1)
    
    # 0번 그룹부터 탐색하며 조건에 맞는 그룹을 찾는다.
    for i in range(0, len(group)):
        # 비교 그룹이 기존 그룹보다 큰 그룹인 경우 index를 갱신한다
        # 크기가 같을 경우 처리 과정에 의해 비교 그룹이 무조건 기존 그룹보다 큰 그룹인 것이 보장되므로 갱신한다.
        
        if len(group[i]) > index[0]:
            index = (len(group[i]), i)
        elif len(group[i]) == index[0]:
            cnt = 0
            for j in group[index[1]]:
                if field[j[0]][j[1]] == 0:
                    cnt += 1
            
            for j in group[i]:
                if field[j[0]][j[1]] == 0:
                    cnt -= 1
            if cnt <= 0:
                index = (len(group[i]), i)
                
    # 가장 큰 그룹의 크기가 2 이상이면
    if index[0] >= 2:
        # 먼저 그룹에 속한 블럭들을 모두 지운다. 이때 빈 공간의 값은 -2로 한다.
        for x, y in group[index[1]]:
            field[x][y] = -2
        
        # 지워진 블럭의 갯수 (그룹의 크기)^2 만큼 점수를 더한다.
        score += index[0]**2

        # True 를 리턴한다. (지워진 블럭이 있다는 의미로)
        return True
    # 가장 큰 그룹의 크기가 2 미만이라면 더이상 그룹이 없다는 의미이므로, False 를 리턴한다.
    else: return False

def gravity():
    for y in range(N):
        move = [0 for _ in range(N)]
        for x in range(N - 1, 0, -1):
            if field[x - 1][y] != -1:
                if field[x][y] == -2: move[x - 1] = move[x] + 1
                else: move[x - 1] = move[x]
        for x in range(N - 2, -1, -1):
            if move[x] and field[x][y] >= 0:
                field[x + move[x]][y] = field[x][y]
                field[x][y] = -2

def rotate():
    global field
    t_field = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            t_field[i][j] = field[j][N - i - 1]
    field = t_field
def t():
    for i in field:
        print(i)
    print()

while True:
    grouping()
    if delete_block():
        gravity()
        rotate()
        gravity()
    else:break

print(score)