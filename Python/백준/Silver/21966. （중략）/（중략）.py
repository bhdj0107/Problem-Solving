N = int(input())
inp = input()
if N <= 25: print(inp)
else:
  mid = inp[11:-11]
  point = mid.count('.')
  if point == 0:
    print(inp[:11] + "..." + inp[-11:])
  elif point == 1:
    if mid[0] == '.' or mid[-1] == '.':
      print(inp[:11] + "..." + inp[-11:])
    else:
      print(inp[:9] + '......' + inp[-10:])
  else:
    print(inp[:9] + '......' + inp[-10:])