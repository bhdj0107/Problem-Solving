import sys
N = int(sys.stdin.readline())
tower = [[N - i + 1for i in range(N + 1)],[N + 1],[N + 1]]
position = {i + 1:0 for i in range(N)}
adder = N % 2 + 1
ans = []
def move(n):
    global position
    global tower
    global ans
    pos = position[n]
    block = tower[pos].pop()
    idx = (pos + adder) % 3
    while True:
        if tower[idx][-1] > block:
            ans.append((pos + 1, idx + 1))
            tower[idx].append(block)
            position[block] = idx
            break
        else:
            idx = (idx + adder) % 3

def processing(n):
    if n == 1:
        move(1)
    else:
        move(n)
        for i in range(1, n):
            processing(i)
for i in range(1, N + 1):
    processing(i)

print(len(ans))
for i, j in ans:
    print(i, j)