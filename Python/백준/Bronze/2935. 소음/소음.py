import sys
a = int(sys.stdin.readline())
op = sys.stdin.readline().rstrip()
b = int(sys.stdin.readline())
if op == "*":
    print(a*b)
else:
    print(a+b)
