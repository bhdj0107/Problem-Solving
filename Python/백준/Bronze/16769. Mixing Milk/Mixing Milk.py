import sys
c1, m1 = map(int, sys.stdin.readline().split())
c2, m2 = map(int, sys.stdin.readline().split())
c3, m3 = map(int, sys.stdin.readline().split())

data = [[c1, m1], [c2, m2], [c3, m3]]
def zeroorplus(i):
    if i < 0:
        return 0
    else:
        return i

for i in range(100):
    if data[(i+1) % 3][0] < data[i % 3][1] + data[(i+1) % 3][1]:
        data[i % 3][1] = data[i % 3][1] + data[(i+1) % 3][1] - data[(i+1) % 3][0]
        data[(i+1) % 3][1] = data[(i+1) % 3][0]
    else:
        data[(i+1) % 3][1] = data[i % 3][1] + data[(i+1) % 3][1]
        data[i % 3][1] = 0
        
for i in data:
    print(i[1])