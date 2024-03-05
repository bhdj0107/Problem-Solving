import sys
data = {0, 132, 6, 138, 12, 144, 18, 150, 24, 156, 30, 162, 36, 168, 42, 174, 48, 180, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126}

for line in sys.stdin:
    if int(line) in data:
        print("Y")
    else:
        print("N")
