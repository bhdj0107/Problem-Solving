import sys
inp = []
dic = {}
for i in range(8):
    dic[i] = int(sys.stdin.readline())
    inp.append(dic[i])
inp.sort()
print(sum(inp[-5:]))
for i in range(8):
    if dic[i] in inp[-5:]:
        if i != 7:
            print(i + 1, end=" ")
        else:
            print(i + 1, end="")