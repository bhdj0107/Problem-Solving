import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = {}
    vsted = set()
    for i in range(N):
        arr[i + 1] = int(sys.stdin.readline())
    idx = arr[1]
    while 1:
        if idx in vsted:
            break
        else:
            vsted.add(idx)
            idx = arr[idx]      
    if N in vsted:
        idx = arr[1]
        cnt = 0
        while 1:
            if idx == N:
                cnt += 1
                break
            else:
                idx = arr[idx]
                cnt += 1
        print(cnt)
    else:
        print(0)