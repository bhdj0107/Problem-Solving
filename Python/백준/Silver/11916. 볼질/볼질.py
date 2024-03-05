import sys

N = int(sys.stdin.readline())
inp = tuple(map(int, sys.stdin.readline().split()))
score = 0
cnt = 0
base = [0, 0, 0]
for i in inp:
    pok = False
    if i == 1:
        cnt += 1
    elif i == 2:
        cnt = 4
    else:
        cnt += 1
        pok = True

    if pok:
        if base[2]:
            score += 1
        base = [0, base[0], base[1]]

    if cnt == 4:
        cnt = 0
        if base == [1, 1, 1]:
            score += 1
        elif base == [1, 1, 0]:
            base = [1, 1, 1]
        elif base == [1, 0, 1]:
            base = [1, 1, 1]
        elif base == [1, 0, 0]:
            base = [1, 1, 0]
        elif base == [0, 1, 1]:
            base = [1, 1, 1]
        elif base == [0, 1, 0]:
            base = [1, 1, 0]
        elif base == [0, 0, 1]:
            base = [1, 0, 1]
        elif base == [0, 0, 0]:
            base = [1, 0, 0]
print(score)
        