import sys
total = 0
heights = []
for _ in range(9):
    temp = int(sys.stdin.readline())
    heights.append(temp)
    total += temp
heights.sort()
for i in range(8):
    for j in range(i, 9):
        if total - heights[i] - heights[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(heights[k])
            exit()