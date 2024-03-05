import sys
N, K = map(int, sys.stdin.readline().split())
table = [i for i in range(N, 1, -1)]
remove_set = set()
def remove(n):
    global remove_set
    remove_set.add(n)
    return len(remove_set) == K

while table:
    num = table.pop()
    if num in remove_set:
    	continue
    remove_set.add(num)
    if K == len(remove_set):
    	print(num)
    	break
    r = num * 2
    i = 2
    while r <= N:
        if remove(r):
            print(r)
            exit()
        i += 1
        r = num * i