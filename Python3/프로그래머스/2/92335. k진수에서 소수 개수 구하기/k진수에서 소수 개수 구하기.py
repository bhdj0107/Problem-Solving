from collections import deque
from math import sqrt

def changeNumberSystem(num, base):
    q = deque()
    while num >= base:
        mok, namuzi = num // base, num % base
        q.appendleft(str(namuzi))
        num = mok
    if num: q.appendleft(str(num))
    return ''.join(q)

def isPrime(n):
    if n == '': return False
    n = int(n)
    if n == 0: return False
    elif n == 1: return False
    elif n == 2: return True
    elif n % 2 == 0: return False
    sq = int(sqrt(n))
    for i in range(2, sq + 1):
        if not n % i: return False
    return True

def solution(n, k):
    return sum([isPrime(p) for p in changeNumberSystem(n, k).split('0')])
