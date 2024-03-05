import sys
N = int(sys.stdin.readline())

if (N % 7) == 0 or (N % 7) == 2:
    print("CY")
    exit()
print("SK")