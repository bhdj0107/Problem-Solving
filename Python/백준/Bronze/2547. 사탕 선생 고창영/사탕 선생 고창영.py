import sys
N = int(sys.stdin.readline())
for _ in range(N):
    sys.stdin.readline()
    n = int(sys.stdin.readline())
    inp = 0
    for _ in range(n):
        inp += int(sys.stdin.readline())
    if inp % n == 0:
        print("YES")
    else:
        print("NO")