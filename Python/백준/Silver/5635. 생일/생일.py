import sys

birth = {}
N = int(sys.stdin.readline())
for _ in range(N):
    Name, D, M, Y = sys.stdin.readline().split()
    D, M, Y = map(int, (D, M, Y))
    if Y not in birth.keys():
        birth[Y] = {}
    if M not in birth[Y].keys():
        birth[Y][M] = {}
    birth[Y][M][D] = Name

Y = max(birth.keys())
M = max(birth[Y].keys())
D = max(birth[Y][M].keys())
print(birth[Y][M][D])

Y = min(birth.keys())
M = min(birth[Y].keys())
D = min(birth[Y][M].keys())
print(birth[Y][M][D])