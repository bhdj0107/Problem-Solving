import sys
N = int(sys.stdin.readline())
temp = set(tuple(map(int, sys.stdin.readline().split())))
a = sorted(list(temp))
for i in a[:-1]:
    print(str(i)+" ", end='')
print(a[-1])