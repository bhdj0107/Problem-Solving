import sys
N = int(sys.stdin.readline())
ans = ""
temp_1 = [[] for _ in range(N + 1)]
temp_2 = {}
for _ in range(N):
    inp = sys.stdin.readline().rstrip()
    if inp not in temp_2.keys():
        temp_2[inp] = 0
        temp_1[0].append(inp)
    temp_2[inp] += 1
    idx = temp_2[inp] - 1
    del temp_1[idx][temp_1[idx].index(inp)]
    temp_1[temp_2[inp]].append(inp)
    
for i in range(N, -1, -1):
  if temp_1[i] != []:
    temp_1[i].sort()
    print(temp_1[i][0])
    exit()