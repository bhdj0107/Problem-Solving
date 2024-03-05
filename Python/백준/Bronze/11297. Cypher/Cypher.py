import sys
temp = {}
for i in range(ord('z') + 1 - ord('a')):
    temp[chr(ord('a') + i)] = i
    temp[i] = chr(ord('a') + i)

while 1:
    N = sum(map(int, sys.stdin.readline().split()))
    if N == 0:
        exit()
    else:
        N = (N % 25) + 1
        inp = sys.stdin.readline().rstrip()
        for i in inp:
            if i in temp.keys():
                tt = temp[i] - N
                if tt < 0:
                    tt += 26
                print(temp[tt], end='')
            else:
                print(i, end='')
        print("")