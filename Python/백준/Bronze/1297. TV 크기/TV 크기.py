import sys
inch, hori, vert = map(int, sys.stdin.readline().split())
x = 0
inch = inch * inch
x = (inch / (hori * hori + vert * vert)) ** 0.5

hori = int((hori * x) // 1)
vert = int((vert * x) // 1)

print(hori, vert)
