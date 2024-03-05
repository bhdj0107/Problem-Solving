import sys
def isPrime(num):
    i = 2
    while i * i < num:
        if num % i == 0:
            return False
        i = i + 1
    return True

inp = sys.stdin.readline().split()
if isPrime(int(inp[1] + inp[0])) and isPrime(int(inp[0])):
    print("Yes")
else:
    print("No")