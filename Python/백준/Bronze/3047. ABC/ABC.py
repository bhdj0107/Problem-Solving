import sys
abc = list(map(int, sys.stdin.readline().split()))
for i in range(2):
    for j in range(i+1, 3):
        if abc[i] > abc[j]:
            abc[i] , abc[j] = abc[j], abc[i]

abc_dict = {"A" : 0, "B" : 1, "C" : 2}
inp = sys.stdin.readline()
for i in range(3):
    print(abc[abc_dict[inp[i]]], end=' ')