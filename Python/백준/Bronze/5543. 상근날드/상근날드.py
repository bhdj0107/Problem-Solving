import sys
h_min = 2001
d_min = 2001
for _ in range(3):
    h_min = min(h_min, int(sys.stdin.readline()))
for _ in range(2):
    d_min = min(d_min, int(sys.stdin.readline()))
    
print(h_min + d_min - 50)