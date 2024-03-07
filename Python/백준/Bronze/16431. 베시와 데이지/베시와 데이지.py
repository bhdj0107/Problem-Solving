import sys
bessie = tuple(map(int,sys.stdin.readline().split()))
daisy = tuple(map(int,sys.stdin.readline().split()))
john = tuple(map(int,sys.stdin.readline().split()))

b_j = max(abs(bessie[0] - john[0]), abs(bessie[1] - john[1]))
d_j = abs(daisy[0] - john[0]) + abs(daisy[1] - john[1])
if b_j < d_j:
    print("bessie")
elif b_j > d_j:
    print("daisy")
else:
    print("tie")