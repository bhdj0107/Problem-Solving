import sys
N = int(sys.stdin.readline())
data = [0]
for _ in range(N): data.append(int(sys.stdin.readline()))
data.append(0)
if N == 1: print(1)
elif N == 2:
    if data[1] == max(data): print(1)
    else: print(2)
else:
    for i in range(1, N + 1):
        # 1 ㅅ 모양
        if data[i - 1] < data[i] and data[i] > data[i + 1]: print(i)
        # 2 r 모양
        if data[i - 1] < data[i] and data[i] == data[i + 1]: print(i)
        # 3 ㄱ 모양
        if data[i - 1] == data[i] and data[i] > data[i + 1]: print(i)
        # 4 ㅡ 모양
        if data[i - 1] == data[i] and data[i] == data[i + 1]: print(i)