# 2021 06 13 0915 start
import sys
N = int(sys.stdin.readline())
states = [(1,2),(9,3),(4,9),(1,2),(5,9),(5,6),(1,7),(8,7),(5,3)]
for _ in range(N):
    inp = sys.stdin.readline().rstrip()
    idx = 0
    state = 0
    while state != 9 and idx < len(inp):
        state = states[state][int(inp[idx])]
        idx += 1
    if state == 3 or state == 6 or state == 7:
        print("YES")
    else: print("NO")