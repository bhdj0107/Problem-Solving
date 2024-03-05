import sys
end = set()
end.update("0123456789")
for line in sys.stdin:
    C = set()
    N = int(line)
    for i in range(1, 999999999):
        C.update(str(i * N))
        if C == end:
            print(i)
            break