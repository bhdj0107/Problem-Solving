import sys
N = int(sys.stdin.readline())
inp = []
while True:
    if len(inp) == N:
        break
    else:
        inp.extend(list(map(str, sys.stdin.readline().split())))
inp = "".join(inp)
i = 0
while True:
    if str(i) not in inp:
        print(i)
        break
    i += 1
