import sys
input = sys.stdin.readline
while True:
    tmp = input().rstrip()
    if tmp == '-1':
        break
    inp = set(map(int, tmp.split()))
    cnt = 0
    for i in inp:
        if i * 2 in inp:
            cnt += 1
    print(cnt - 1)