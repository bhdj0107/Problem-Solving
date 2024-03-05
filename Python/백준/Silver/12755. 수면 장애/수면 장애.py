import sys
N = int(sys.stdin.readline())
for i in range(1, 100000000):
    N -= len(str(i))
    if N <= 0: 
        ans = i
        break
print(str(i)[N - 1])