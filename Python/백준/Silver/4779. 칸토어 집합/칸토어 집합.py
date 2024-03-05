import sys
for line in sys.stdin:
    table = '-'
    N = int(line)
    for _ in range(N):
        table = table + "".join([" " for _ in range(len(table))]) + table
    print(table)