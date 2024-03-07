# 2021 07 04 1521
import sys
A = int(sys.stdin.readline())
if A == 1: print(1)
elif A == 2: print(2)
else:
    A = A - 2
    A = A % 8
    if 0 <= A < 4:
        print(A + 2)
    else:
        print(8 - A)