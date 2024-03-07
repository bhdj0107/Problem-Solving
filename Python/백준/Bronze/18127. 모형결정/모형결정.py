import sys
a, b = map(int, sys.stdin.readline().split())
cnt = 1
for i in range(b):
    add_cnt = i + 2
    add_cnt = add_cnt + ((add_cnt - 1) * (a - 3))
    cnt += add_cnt

print(cnt)