import sys
temp = set()
temp.update([i for i in range(1, 31)])

for _ in range(28):
    N = int(sys.stdin.readline())
    temp.remove(N)

for v in temp:
    print(v)