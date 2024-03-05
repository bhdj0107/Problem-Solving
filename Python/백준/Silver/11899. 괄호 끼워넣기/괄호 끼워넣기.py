import sys
inp = sys.stdin.readline().rstrip()
count = 0
ans = 0
cnt = {'(' : 1, ')' : -1}
for i in inp:
    count += cnt[i]
    if count < 0:
        ans += 1
        count = 0
print(ans + count)