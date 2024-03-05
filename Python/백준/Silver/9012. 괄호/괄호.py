import sys
N = int(sys.stdin.readline())
for _ in range(N):
    C = 0
    inp = sys.stdin.readline().rstrip()
    for i in inp:
        if i == '(':
            C += 1
        else:
            C -= 1
            if C == -1:
                break
    if C == 0:
        print("YES")
    else:
        print("NO")
