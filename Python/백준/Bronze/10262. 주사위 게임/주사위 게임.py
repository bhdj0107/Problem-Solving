import sys
Ga1, Gb1, Ga2, Gb2 = map(int, sys.stdin.readline().split())
Ea1, Eb1, Ea2, Eb2 = map(int, sys.stdin.readline().split())

G1 = ((Gb1 - Ga1 + 1) * (2 * Ga1 + (Gb1 - Ga1)) // 2) / (Gb1 - Ga1 + 1)
G2 = ((Gb2 - Ga2 + 1) * (2 * Ga2 + (Gb2 - Ga2)) // 2) / (Gb2 - Ga2 + 1)

E1 = ((Eb1 - Ea1 + 1) * (2 * Ea1 + (Eb1 - Ea1)) // 2) / (Eb1 - Ea1 + 1)
E2 = ((Eb2 - Ea2 + 1) * (2 * Ea2 + (Eb2 - Ea2)) // 2) / (Eb2 - Ea2 + 1)

if G1 + G2 > E1 + E2:
    print("Gunnar")
elif G1 + G2 < E1 + E2:
    print("Emma")
else:
    print("Tie")