import sys
from math import sqrt

def a():
  all_prime = []
  prime_table = [True for _ in range(1000001)]
  prime_table[0] = False
  prime_table[1] = False
  for i in range(2, 1000001):
    if prime_table[i]:
      all_prime.append(i)
      for j in range(2, 1000001):
        if i * j <= 1000000:
          prime_table[i * j] = False
        else: break
  
  while True:
    N = int(sys.stdin.readline())
    if N == 0: break
    a, b = -1, -1
    for i in all_prime:
      if i < 500001:
        if prime_table[N - i]:
          a, b = i, N - i
          break
      else: 
        break
    if a == -1:
      print("Goldbach's conjecture is wrong.")
    else:
      print(N, "=", a, "+", b)
a()