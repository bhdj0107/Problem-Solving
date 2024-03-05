import sys

N = int(sys.stdin.readline())
inp = []
for _ in range(N):
    inp.append(sys.stdin.readline().rstrip())

chk = {}
for i in range(N):
    temp = {0: 0}
    t_chk = ""
    for j in range(len(inp[i])):
        aa = inp[i][j]
        try:
            t_chk = t_chk + str(temp[inp[i][j]])
        except:
            temp[inp[i][j]] = max(temp.values()) + 1
            t_chk = t_chk + str(temp[inp[i][j]])
    try:
        chk[t_chk] += 1
    except:
        chk[t_chk] = 0

ans = 0
for i in chk.values():
    for j in range(1, i+1):
        ans += j

print(ans)