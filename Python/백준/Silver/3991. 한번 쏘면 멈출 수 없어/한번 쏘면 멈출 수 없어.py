import sys
h, w, c = map(int, sys.stdin.readline().split())
color = tuple(map(int, sys.stdin.readline().split()))
table = [[0 for _ in range(w)] for _ in range(h)]
cnt = 0
for i in range(c):
    for j in range(color[i]):
        table[cnt % h][cnt // h] = str(i + 1)
        cnt += 1
        
for i in table:
    print("".join(i))