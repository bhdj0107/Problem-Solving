import sys
A = tuple(map(int, sys.stdin.readline().split()))
B = tuple(map(int, sys.stdin.readline().split()))
C = [0,0,-1]
for i in range(10):
    T = A[i] - B[i]
    if T > 0:
        C[0] += 1
        C[2] = 0
    elif T < 0:
        C[1] += 1
        C[2] = 1
sA = C[0] * 3 + 10 - (C[0] + C[1])
sB = C[1] * 3 + 10 - (C[0] + C[1])
print(sA, sB)
if C[2] == -1:
    print("D")
else:
    if sA > sB:
        print("A")
    elif sB < sA:
        print("B")
    else:
        if C[2] == 1:
            print("B")
        else:
            print("A")
