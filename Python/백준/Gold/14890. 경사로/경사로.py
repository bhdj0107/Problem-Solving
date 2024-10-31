import sys

# f = open('./input.txt', 'r')
# sys.stdin.readline = f.readline

N, L = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def check_is_path_passable(path_idx, isHorizontal):
    
    
    path = []
    if isHorizontal:
        for i in range(N):
            path.append(field[path_idx][i])
    else:
        for i in range(N):
            path.append(field[i][path_idx])

    isRampSet = [False for _ in range(N)]
    for i in range(N - 1):
        diff = abs(path[i] - path[i + 1])
        if diff == 1:
            # 왼쪽이 더 높은 경우
            if path[i] > path[i + 1]:
                
                # 이미 오른쪽에 경사로가 설치되어 있는 경우
                if isRampSet[i + 1]: return False
                
                # 빈 공간이 있는 경우
                else:
                    # L만큼의 연속한 빈 공간이 있는 경우
                    isSettable = True
                    for j in range(i + 1, i + 1 + L):
                        # 필드를 벗어나는 경우 안됨
                        if not j < N: 
                            isSettable = False
                            break
                        # 설치할 자리에 뭐가 있어도 안됨
                        if isRampSet[j]:
                            isSettable = False
                            break
                        
                    # 경사로 설치 자리가 확보되어 있으면
                    if isSettable:
                        # L 길이의 경사로 설치
                        for j in range(L):
                            isRampSet[i + 1 + j] = True
                    else: return False
                    
                        
            # 오른쪽이 더 높은 경우
            else:
                # 이미 왼쪽에 경사로가 설치되어 있는 경우
                if isRampSet[i]: return False
                
                # 빈 공간이 있는 경우
                else:
                    # L만큼의 연속한 빈 공간이 있는 경우
                    isSettable = True
                    for j in range(i, i - L, -1):
                        # 필드를 벗어나는 경우 안됨
                        if not j >= 0: 
                            isSettable = False
                            break
                        # 설치할 자리에 뭐가 있어도 안됨
                        if isRampSet[j]:
                            isSettable = False
                            break
                        
                    # 경사로 설치 자리가 확보되어 있으면
                    if isSettable:
                        # L 길이의 경사로 설치
                        for j in range(L):
                            isRampSet[i - j] = True
                    else: return False
        elif diff > 1: return False
        
    return True

count = 0
for i in range(N):
    count += int(check_is_path_passable(i, True))
    count += int(check_is_path_passable(i, False))
    
print(count)