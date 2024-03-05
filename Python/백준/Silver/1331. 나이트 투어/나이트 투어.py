import sys
temp = {chr(i):[1 for _ in range(6)] for i in range(ord('A'), ord('F') + 1)}
s_inp = sys.stdin.readline().rstrip()
temp[s_inp[0]][int(s_inp[1]) - 1] = 0
b_inp = s_inp
a = 0
for _ in range(35):
    inp = sys.stdin.readline().rstrip()
    if b_inp == "":
        temp[inp[0]][int(inp[1]) - 1] = 0
    elif abs(ord(b_inp[0]) - ord(inp[0])) == 2 and abs(int(b_inp[1]) - int(inp[1])) == 1:
        temp[inp[0]][int(inp[1]) - 1] = 0             
    elif abs(ord(b_inp[0]) - ord(inp[0])) == 1 and abs(int(b_inp[1]) - int(inp[1])) == 2:
        temp[inp[0]][int(inp[1]) - 1] = 0             
    else:
        a += 1
    b_inp = inp
        

for i in range(ord('A'), ord('F') + 1):
    a += sum(temp[chr(i)])

if a == 0 and abs(ord(s_inp[0]) - ord(inp[0])) == 2 and abs(int(s_inp[1]) - int(inp[1])) == 1:
    print("Valid")
elif a == 0 and abs(ord(s_inp[0]) - ord(inp[0])) == 1 and abs(int(s_inp[1]) - int(inp[1])) == 2:
    print("Valid")
else:
    print("Invalid")