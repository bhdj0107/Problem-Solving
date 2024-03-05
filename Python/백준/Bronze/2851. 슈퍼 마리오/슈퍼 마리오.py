import sys
input = sys.stdin.readline
ans = 0
inp = []
for i in range(10):
    inp.append(int(input()))
for n in inp:
    if ans + n > 100:
        if abs(ans - 100) >= abs(ans + n - 100):
            print(ans + n)
        else:
            print(ans)
        exit()
    ans += n
print(ans)