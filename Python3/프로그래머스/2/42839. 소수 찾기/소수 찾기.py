from itertools import permutations
from math import sqrt

def isPrime(n):
    if n == 0: return False
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    sq = int(sqrt(n))
    for i in range(2, sq + 1):
        if n % i == 0: return False
    return True

def solution(numbers):
    maxLen = len(numbers)
    primable = set()
    for i in range(1, maxLen + 1):
        for target in permutations(numbers, i):
            if target[0] != 0:
                target = ''.join(target)
                if isPrime(int(target)): 
                    primable.add(int(target))
    return len(primable)