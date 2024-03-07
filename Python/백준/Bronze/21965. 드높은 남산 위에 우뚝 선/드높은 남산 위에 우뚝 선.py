N = int(input())
inp = list(map(int, input().split()))
inp.append(-1)
idx = 0

if N == 1:
    print("YES")
elif N == 2:
    if inp[0] < inp[1]:
        print("YES")
    else: print("NO")
else:
    while 1:
        if not inp[idx] < inp[idx + 1]: break
        idx += 1
    while idx < N:
        if not inp[idx] > inp[idx + 1]: break
        idx += 1
    if idx == N: print("YES")
    else: print("NO")
    
  