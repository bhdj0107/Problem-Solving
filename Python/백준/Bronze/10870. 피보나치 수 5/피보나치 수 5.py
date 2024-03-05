import sys
dic = {}
N = int(sys.stdin.readline())
def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        try:
            a = dic[n-1]
        except:
            dic[n-1] = Fibonacci(n-1)
            a = dic[n-1]
        try:
            b = dic[n-2]
        except:
            dic[n-2] = Fibonacci(n-2)
            b = dic[n-2]
        return a + b
print(Fibonacci(N))