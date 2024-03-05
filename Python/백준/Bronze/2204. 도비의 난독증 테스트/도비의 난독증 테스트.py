import sys
ctoi = {'*' : 30}
for i in range(ord('z') - ord('a') + 1):
    ctoi[chr(i+ord("a"))] = i
    ctoi[chr(i+ord("A"))] = i
while 1:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    temp = ["" for _ in range(N)]
    for i in range(N):
        temp[i] = sys.stdin.readline().rstrip()
    ans = "*"
    for s in temp:
        for i in range(min(len(ans), len(s))):
            if ctoi[ans[i]] > ctoi[s[i]]:
                ans = s
                break
            elif ctoi[ans[i]] == ctoi[s[i]]:
                if i == min(len(ans), len(s)) - 1:
                    if len(ans) > len(s):
                        ans = s
                continue
            else:
                break
    print(ans)