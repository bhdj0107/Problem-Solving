import sys
N = int(sys.stdin.readline())
inp = []
cnt = 0
for _ in range(N):
    inp.append(tuple(sys.stdin.readline().split()))

for i in range(1, 101):
    tmp = i
    for op in inp:
        if op[0] == "ADD":
            tmp += int(op[1])
        if op[0] == "SUBTRACT":
            tmp -= int(op[1])
            if tmp < 0:
                cnt += 1
                break
        if op[0] == "DIVIDE":
            if tmp % int(op[1]):
                cnt += 1
                break
            tmp = tmp // int(op[1])
        if op[0] == "MULTIPLY":
            tmp *= int(op[1])

print(cnt)