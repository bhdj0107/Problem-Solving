import sys
C = int(sys.stdin.readline())
for i in range(C):
    inp = list(map(int, sys.stdin.readline().split()))
    temp = [0 for _ in range(101)]
    for j in inp[1:]:
        temp[j] += 1
    avg = sum(inp[1:]) // inp[0]
    print(str(format(round(sum(temp[avg+1:]) / inp[0] * 100, 3), ".3f")) + "%")