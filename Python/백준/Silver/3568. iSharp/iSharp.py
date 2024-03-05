import sys
S = sys.stdin.readline().rstrip()
S_list = S.split()
for tt in S_list[1:]:
    temp = tt[:-1]
    ans = S_list[0]
    right, left = 0, 0
    for i in range(len(temp) - 1, -1, -1):
        if temp[i] in "&*":
            ans = ans + temp[i]
        elif temp[i] == "[":
            ans = ans + "]"
        elif temp[i] == "]":
            ans = ans + "["
        else:
        	right = i
        	break
    for i in range(len(temp)):
    	if temp[i] in "&*[]":
    		ans = ans + temp[i]
    	else:
    		left = i
    		break
    print(ans + " " + temp[left:right+1] + ";")