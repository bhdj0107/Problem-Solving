import sys
N = sys.stdin.readline().rstrip()
if N[1] == 'x':
    print(int(N, 16))
elif N[0] == '0':
    N = N[0] + 'o' + N[1:]
    print(int(N, 8))
else:
    print(N)