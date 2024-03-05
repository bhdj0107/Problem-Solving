import sys
table = [0 for _ in range(21)]
cnt = 0
chk = {0 : 0}
for i in range(1, 5):
  for j in range(1, 5 * i + 1):
    cnt = cnt + 1
    chk[cnt] = j
  for j in range(5 * i - 1, -1, -1):
    cnt = cnt + 1
    chk[cnt] = j

N = int(sys.stdin.readline())
N = N % 100
if chk[N] == 0:
  print(0)
elif chk[N] > 0 and chk[N] <= 5:
  print(1)
elif chk[N] > 5 and chk[N] <= 10:
  print(2)
elif chk[N] > 10 and chk[N] <= 15:
  print(3)
elif chk[N] > 15 and chk[N] <= 20:
  print(4)