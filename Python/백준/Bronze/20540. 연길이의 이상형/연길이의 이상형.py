# 2020 07 02 1905 start
import sys
inp = sys.stdin.readline().rstrip()
ans = {}
for i in range(8):
    a, b = "ESTJINFP", "INFPESTJ"
    ans[a[i]] = b[i]
for i in inp:
    print(ans[i], end='')
print()