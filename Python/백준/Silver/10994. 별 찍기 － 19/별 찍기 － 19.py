import sys
N = int(sys.stdin.readline())
length = (N - 1) * 4 + 1
ans = [[' ' for _ in range(length)] for _ in range(length)]
s, e = 0, length - 1
while s != e:
    # 가로
    for i in range(e - s + 1):
        ans[s][s + i] = '*'
        ans[e][s + i] = '*'
    # 세로
    for i in range(e - s + 1):
        ans[s + i][s] = '*'
        ans[s + i][e] = '*'
    
    s += 2
    e -= 2
ans[s][s] = '*'
for i in ans:
    print(''.join(i))