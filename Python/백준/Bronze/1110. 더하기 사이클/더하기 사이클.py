import sys
input = sys.stdin.readline
n = input().rstrip()
A = n
cnt = 1
tmp = 0
for i in A:
    tmp += int(i)
A = A[-1] + str(tmp)[-1]
while True:
    if int(A) == int(n):
        break
    tmp = 0
    for i in A:
        tmp += int(i)
    A = A[-1] + str(tmp)[-1]
    cnt += 1
print(cnt)