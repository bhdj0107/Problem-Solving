import sys
temp = {}
count = [0 for _ in range(ord('a'), ord('z') + 1)]
         
for i in range(ord('a'), ord('z') + 1):
    temp[chr(i)] = i - ord('a')
for i in range(ord('A'), ord('Z') + 1):
    temp[chr(i)] = i - ord('A')
    temp[i - ord('A')] = chr(i)

inp = sys.stdin.readline().rstrip()
for i in inp:
    count[temp[i]] += 1


idx = count.index(max(count))
mx = count[idx]
del count[idx]
if mx in count:
    print("?")
else:
    print(temp[idx])