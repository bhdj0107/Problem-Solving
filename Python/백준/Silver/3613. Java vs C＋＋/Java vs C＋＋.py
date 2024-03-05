import sys
lower_set = set()
upper_set = set()
Cap = False
ans = ""
for i in range(26):
    lower_set.add(chr(ord('a') + i))
for i in range(26):
    upper_set.add(chr(ord('A') + i))

inp = sys.stdin.readline().rstrip()
if '_' in inp:
    if inp[0] == '_' or inp[-1] == '_':
        print("Error!")
        exit()
    for i in inp:
        if Cap:
            if i in lower_set:
                    ans = ans + i.upper()
                    Cap = False
            else:
                print("Error!")
                exit()
        else:
            if i in lower_set:
                    ans = ans + i
            elif i == '_':
                Cap = True
            else:
                print("Error!")
                exit()
else:
    if inp[0] in upper_set:
        print("Error!")
        exit()
    for i in inp:
        if i in lower_set:
            ans = ans + i
        elif i in upper_set:
            ans = ans + '_' + i.lower()
        else:
            print("Error!")
            exit()
print(ans)