import sys
A, B = map(int, sys.stdin.readline().split())
dic = [0, 1]

cnt = 2
while len(dic) < 1000:
    for i in range(cnt):
        dic.append(dic[-1] + cnt)
    cnt += 1
print(dic[B] - dic[A - 1])
    
    
