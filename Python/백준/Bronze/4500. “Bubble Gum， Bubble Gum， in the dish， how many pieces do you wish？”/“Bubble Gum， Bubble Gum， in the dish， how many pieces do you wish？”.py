import sys
T = int(sys.stdin.readline())
for _ in range(T):
    name = sys.stdin.readline().split()
    dic = {}
    for i in range(len(name)):
        dic[i] = name[i]
        dic[name[i]] = i
    
    
    print(dic[(dic[sys.stdin.readline().rstrip()]+ int(sys.stdin.readline()) - 1) % len(name)])