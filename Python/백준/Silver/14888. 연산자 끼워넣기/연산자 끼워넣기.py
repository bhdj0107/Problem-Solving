import sys


def postfix(ops):
    loopCnt = (len(ops) - 3) // 2
    first = int(eval(str(ops[0]) + ops[1] + str(ops[2])))
    for i in range(loopCnt):
        first = int(eval(str(first) + ops[1 + (2 * (i + 1))] + str(ops[2 + (2 * (i + 1))])))
    return first

stack = []
ops = []
maxValue = -1e+32
minValue = 1e+32

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
operatorCnt = list(map(int, sys.stdin.readline().split()))
opMap = ('+', '-', "*", '/')

def dfs(D):
    global maxValue
    global minValue
    global operatorCnt
    global ops
    if D == N - 1:
        ops.append(nums[-1])
        tmp = postfix(ops)
        minValue = min(minValue, tmp)
        maxValue = max(maxValue, tmp)
        ops.pop()
    else:
        ops.append(nums[D])
        for i in range(4):
            if operatorCnt[i] > 0:
                operatorCnt[i] -= 1
                ops.append(opMap[i])
                dfs(D + 1)
                operatorCnt[i] += 1
                ops.pop()
        ops.pop()

dfs(0)
print(maxValue)
print(minValue)