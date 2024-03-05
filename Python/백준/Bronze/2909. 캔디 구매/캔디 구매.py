import sys
A, B = map(int,sys.stdin.readline().split())
if ((A * 10) / (10 ** B)) % 10 >= 5:
    print((A // (10 ** B) + 1) * (10 ** B))
else:
    print((A // (10 ** B)) * (10 ** B))