import sys
sen = "baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan".split()
N = int(sys.stdin.readline())
ans = sen[(N-1) % 14]
if (N-1) % 14 in [2,6,10]:
    if N // 14 >= 3:
        ans = "tu+ru*" + str(N // 14 + 2)
    else:
        ans = ans + "".join(["ru" for _ in range(N // 14)])

if (N-1) % 14 in [3,7,11]:
    if N // 14 >= 4:
        ans = "tu+ru*" + str(N // 14 + 1)
    else:
        ans = ans + "".join(["ru" for _ in range(N // 14)])

print(ans)