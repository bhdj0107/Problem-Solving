import sys
N = int(sys.stdin.readline())
def Fibonacci(n):
    if n <= 0:
        return 1
    else:
        return Fibonacci(n - 1) * n
    
print(Fibonacci(N))