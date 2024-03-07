# 2020 07 02 1856 start
import sys
A, B, C = map(int, sys.stdin.readline().split())
tmp = {A:"Soongsil", B:"Korea", C:"Hanyang"}
if A + B + C >= 100: print("OK")
else: print(tmp[min(A, B, C)])