import sys
a, b, c = map(int, sys.stdin.readline().split())

ans = c - abs(a) - abs(b)
if ans < 0: print("NO")
else:
    if ans % 2 == 0: print("YES")
    else: print("NO")