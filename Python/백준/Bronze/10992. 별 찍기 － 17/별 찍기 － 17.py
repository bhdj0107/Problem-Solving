import sys
N = int(sys.stdin.readline())
print(("".join([" " for _ in range(N - 1)])) + "*")
if not N == 1:
    for i in range(N - 2):
        temp = "".join([" " for _ in range(N - 2 - i)]) + "*"
        temp = temp + "".join([" " for _ in range(2 * i + 1)]) + "*"
        print(temp)
    print("".join("*" for _ in range(N * 2 - 1)))