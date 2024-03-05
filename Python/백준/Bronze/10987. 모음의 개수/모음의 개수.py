import sys
dic = {}
for i in range(ord('a'), ord('z') + 1):
    dic[chr(i)] = 0
dic['a'] = 1
dic['e'] = 1
dic['i'] = 1
dic['o'] = 1
dic['u'] = 1

cnt = 0
inp = sys.stdin.readline().rstrip()
for i in inp:
    cnt += dic[i]
print(cnt)