import sys
from itertools import combinations
from math import inf

N = int(sys.stdin.readline())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
total = set(range(N))
ans = inf

for teamA in combinations(total, N // 2):
    teamA = set(teamA)
    teamB = total - teamA

    scoreA = sum([table[score[0]][score[1]] + table[score[1]][score[0]] for score in combinations(teamA, 2)])
    scoreB = sum([table[score[0]][score[1]] + table[score[1]][score[0]] for score in combinations(teamB, 2)])

    ans = min(ans, abs(scoreA - scoreB))

print(ans)