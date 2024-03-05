import sys
input = sys.stdin.readline

limit = [0, 10]
ans = ("Stan is dishonest", "Stan may be honest")
honest = 1
while True:
    inp = input().rstrip()
    try:
        n = int(inp)
        if n == 0:
            break
    except:
        if inp == "right on":
            if not n in list(range(limit[0], limit[1] + 1)):
                honest = 0
            print(ans[honest])
            limit = [0, 10]
            honest = 1
            continue
        if honest == 0:
            continue
        else:
            if inp == 'too high':
                limit[1] = min(limit[1], n - 1)
            elif inp == 'too low':
                limit[0] = max(limit[0], n + 1)
            if limit[1] < limit[0]:
                honest = 0