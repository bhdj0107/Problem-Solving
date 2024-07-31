import sys
from itertools import product
N = int(sys.stdin.readline())
probabilities = set()
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and k != i:
                probabilities.add((i, j, k))
def sbCount(src, dst):
    s = 0
    b = 0
    for i, n in enumerate(dst):
        for j, m in enumerate(src):
            if n == m:
                if i == j: s += 1
                else: b += 1
    return s, b

for _ in range(N):
    num, s, b = map(int, sys.stdin.readline().split())
    num = list(map(int, list(str(num))))
    newProbs = set()
    for prob in probabilities:
        newS, newB = sbCount(num, prob)
        if s == newS and b == newB:
            newProbs.add(prob)
    probabilities = newProbs
print(len(probabilities))