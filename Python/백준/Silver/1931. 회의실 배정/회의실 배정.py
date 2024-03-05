import sys
N = int(sys.stdin.readline())
me = {}
etc = {}
mt = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    mt = max(mt, b)
    if a == b:
        try:
            me[b] += 1
        except:
            me[b] = 1
    else:
        try: etc[b] = max(etc[b], a)
        except: etc[b] = a
        
end = 0
cnt = 0
for i in range(mt + 1):
    if i < end: continue
    #print(cnt ,i)
    tmp = cnt
    if i in me: cnt += me[i]
    if i in etc: cnt += int(etc[i] >= end)
    if tmp != cnt: end = i
print(cnt)