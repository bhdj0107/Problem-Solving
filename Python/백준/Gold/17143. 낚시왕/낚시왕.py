import sys

R, C, M = map(int, sys.stdin.readline().split())
dc = (0, 0, 0, 1, -1)
dr = (0, -1, 1, 0, 0)
cnt = 0
sharks = {}

for i in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    sharks[(r - 1, c - 1)] = (s, d, z, r - 1, c - 1)

sam_r = {}
sam_c = {}
for i in range(R):
    sam_r[i] = i
for i in range(R - 1):
    sam_r[2*R - 2 - i - 1] = i + 1
for i in range(C):
    sam_c[i] = i
for i in range(C - 1):
    sam_c[2*C - 2 - i - 1] = i + 1


def bigger(A, B):
    if A[2] > B[2]:
        return A
    else:
        return B


def move():
    global sharks
    t_sharks = {}
    for tr, tc in sharks.keys():
        temp = sharks[(tr, tc)]
        tr = (temp[3] + dr[temp[1]] * temp[0]) % ((R - 1) * 2)
        tc = (temp[4] + dc[temp[1]] * temp[0]) % ((C - 1) * 2)
        if (sam_r[tr], sam_c[tc]) in t_sharks.keys():
            t_sharks[(sam_r[tr], sam_c[tc])] = bigger(temp[:3] + (tr, tc), t_sharks[(sam_r[tr], sam_c[tc])])
        else:
            t_sharks[(sam_r[tr], sam_c[tc])] = temp[:3] + (tr, tc)
    sharks = t_sharks


for man in range(C):
    for row in range(R):
        if (sam_r[row], sam_c[man]) in sharks.keys():
            cnt += sharks[(sam_r[row], sam_c[man])][2]
            del sharks[(sam_r[row], sam_c[man])]
            break
    move()

print(cnt)