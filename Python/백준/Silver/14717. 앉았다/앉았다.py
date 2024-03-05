import sys
A, B = map(int, sys.stdin.readline().split())

box = []
for i in range(1, 11):
    if i != A:
        box.append(i)
    if i != B:
        box.append(i)
if A == B:
    my = 101 * A
else:
    my = (A + B) % 10

total = 153
cnt = 0
for i in range(len(box) - 1):
    for j in range(i + 1, len(box)):
        if box[i] == box[j]:
            boxn = 101 * box[i]
        else:
            boxn = (box[i] + box[j]) % 10
        if boxn < my:
            cnt += 1
print(format(cnt / total, ".3f"))