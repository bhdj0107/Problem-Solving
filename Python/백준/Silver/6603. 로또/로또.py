import sys
from itertools import combinations

while True:
    inp = list(map(int, sys.stdin.readline().split()))
    N = inp[0]
    if N == 0: break
    else:
        nums = inp[1:]
        for idxes in combinations(range(len(nums)), 6):
            output = [nums[idxes[i]] for i in range(6)]
            print(output[0],output[1],output[2],output[3],output[4],output[5])
        print()