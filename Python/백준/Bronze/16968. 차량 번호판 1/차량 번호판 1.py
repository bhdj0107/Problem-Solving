import sys
inp = sys.stdin.readline().rstrip()
dic = {"c" : 26, "d" : 10}
cnt = dic[inp[0]]
for i in range(len(inp) - 1):
    if inp[i:i+2] == "cc":
        cnt = cnt * 25
    elif inp[i:i+2] == "cd":
        cnt = cnt * 10
    elif inp[i:i+2] == "dc":
        cnt = cnt * 26
    elif inp[i:i+2] == "dd":
        cnt = cnt * 9
print(cnt)