import sys
def Quick_Sort(arr):
    if len(arr) == 2:
        return [min(arr), max(arr)]
    elif len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        idx = round((len(arr)) / 2) - 1
        left = []
        middle = []
        right = []
        for i in arr:
            if i < arr[idx]:
                left.append(i)
            elif i > arr[idx]:
                right.append(i)
            else:
                middle.append(i)
        arr = left + middle + right
        lef = len(left)
        mid = lef + len(middle)
        del left, right, middle
        return Quick_Sort(arr[:lef]) + arr[lef: mid] + Quick_Sort(arr[mid:])

def ans():
    N, M = map(int, sys.stdin.readline().split())
    inp = list(map(int, sys.stdin.readline().split()))
    inp = inp + list(map(int, sys.stdin.readline().split()))
    print(*sorted(inp))

ans()