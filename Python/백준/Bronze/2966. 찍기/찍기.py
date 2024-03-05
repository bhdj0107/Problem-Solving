import sys
input = sys.stdin.readline
N = int(input())
inp = input().rstrip()
ans = ("Adrian", "Bruno", "Goran")
a = (0, 1, 2)
b = (1, 0, 1, 2)
c = (2, 2, 0, 0, 1, 1)

alptonum = {"A":0, "B":1,"C":2}

score = [0,0,0]
for i in range(N):
    if alptonum[inp[i]] == a[i%3]:
        score[0] += 1
    if alptonum[inp[i]] == b[i%4]:
        score[1] += 1
    if alptonum[inp[i]] == c[i%6]:
        score[2] += 1
    
print(max(score))
for i in range(3):
    if score[i] == max(score):
        print(ans[i])