import sys
input = sys.stdin.readline

N = int(input())
children = [[] for _ in range(N + 1)]
inp = tuple(map(int, input().split()))
for i in range(N):
    children[inp[i] + 1].append(i + 1)
remove = set()
remove.add(int(input()) + 1)
skip = set()
while remove:
    idx = remove.pop()
    remove.update(children[idx])
    skip.add(idx)
ans = 0
for i in range(1, N + 1):
    if i in skip:
        continue
    else:
        temp = 0
        for j in children[i]:
            if j in skip:
                temp += 1
        ans += int(temp == len(children[i]))
print(ans)