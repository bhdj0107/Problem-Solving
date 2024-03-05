import sys
total = 0
for _ in range(5):
    N = int(sys.stdin.readline())
    if N < 40:
        total += 8
    else:
        total += N // 5
print(total)