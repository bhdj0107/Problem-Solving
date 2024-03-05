import sys
N = int(sys.stdin.readline())
inp = []
for _ in range(N):
    inp.append(tuple(sys.stdin.readline().split()))
inp.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in inp:
    print(i[0])