import sys
N = int(sys.stdin.readline())
cnt = 0
for _ in range(N):
    inp = sys.stdin.readline().rstrip()
    stack = ['']
    for i in inp:
        if i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if stack == ['']:
        cnt += 1
print(cnt)