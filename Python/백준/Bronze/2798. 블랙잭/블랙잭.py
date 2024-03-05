import sys
N, M = map(int, sys.stdin.readline().split())
Cards = tuple(map(int, sys.stdin.readline().split()))
sum_2 = set()
sum_3 = set()
for i in range(len(Cards)):
    for j in sum_2:
        if j + Cards[i] <= M:
            sum_3.add(j + Cards[i])
    for j in range(i):
        sum_2.add(Cards[i] + Cards[j])

print(max(sum_3))
