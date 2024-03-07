import sys
n, k = map(int, sys.stdin.readline().split())
cnt = 0
dectobin = "0"
i = 0
ans = []
while 1:
    if dectobin == "":
        cnt += 1
        dectobin = str(format(cnt, 'b'))

    if (i % n) == (k - 1):
        ans.append(dectobin[0])
    dectobin = dectobin[1:]
    i += 1
    if len(ans) == 5:
        print(ans[0], ans[1], ans[2], ans[3], ans[4])
        exit()

