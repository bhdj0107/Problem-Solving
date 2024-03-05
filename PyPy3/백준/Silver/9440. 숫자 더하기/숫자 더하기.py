#9440
import sys
while True:
    inp = sys.stdin.readline().rstrip()
    if inp == '0':
        break
    inp = tuple(map(int, inp.split()))
    st = ['', '']
    cnt = 0
    n_cnt = {i:0 for i in range(10)}
    for i in range(1, inp[0] + 1):
        n_cnt[inp[i]] += 1
    for i in range(9, 0, -1):
        for _ in range(n_cnt[i]):
            st[cnt % 2] = str(i) + st[cnt % 2]
            cnt += 1
    for i in range(n_cnt[0]):
        idx = int(min(map(int, st)) == int(st[1]))
        a = int(st[(idx + 1) % 2])
        b = int(st[idx][0] + '0' + st[idx][1:])
        
        st = [str(a), str(b)]
    print(sum(map(int, st)))