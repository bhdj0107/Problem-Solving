N, M = map(int,input().split())
field = [list(map(int, input().split())) for _ in range(N)]

cameras = []
cameras_num = 0
for i in range(N):
  for j in range(M):
    if str(field[i][j]) in '12345':
      cameras.append((i, j, field[i][j]))
      cameras_num += 1
      
def count_unmasked(field):
  return sum([field[i].count(0) for i in range(N)])

answer = N * M
def masker(i, j, d, mask):
  global field
  dx = [1,0,-1,0]
  dy = [0,1,0,-1]

  while True:
    after = (i + dy[d], j + dx[d])
    if after[1] >= 0 and after[1] < M:
      if after[0] >= 0 and after[0] < N:
        # 기존에 마스킹 된 자리인 경우
        if field[after[0]][after[1]] > 9:
          if mask:
            field[after[0]][after[1]] += 1
          else:
            field[after[0]][after[1]] -= 1

        # 아예 빈칸으로 만들어야 하는 경우
        elif field[after[0]][after[1]] == 9:
          if mask:
            field[after[0]][after[1]] += 1
          else:
            field[after[0]][after[1]] = 0

        # 원래 빈칸이었던 경우
        elif field[after[0]][after[1]] == 0:
          if mask:
            field[after[0]][after[1]] = 9
          else:
            field[after[0]][after[1]] = 0

        # 벽인 경우
        elif field[after[0]][after[1]] == 6:
          break
        i, j = after[0], after[1]
      else: break
    else: break
          
        
      
def recursion(D):
  global answer, field, cameras
  if D == cameras_num:
    tmp = count_unmasked(field)
    answer = min(tmp, answer)
  else:
    nowcam = cameras.pop()
    i, j, types = nowcam
    if types == 1:
      directions = [0]
    elif types == 2:
      directions = [0, 2]
    elif types == 3:
      directions = [0, 1]
    elif types == 4:
      directions = [0, 1, 2]
    elif types == 5:
      directions = [0, 1, 2, 3]

    for k in range(4):
      for d in directions:
        d = (d + k) % 4
        masker(i, j, d, True)
      recursion(D+1)
      for d in directions:
        d = (d + k) % 4
        masker(i, j, d, False)
      if types == 5: break
          
    cameras.append(nowcam)

recursion(0)
print(answer)
      