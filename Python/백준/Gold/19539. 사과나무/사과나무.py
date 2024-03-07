import sys
sys.stdin.readline()
s=sum(i//2-i%2 for i in map(int,sys.stdin.readline().split()))
print(['NO',"YES"][s>=0 and s%3==0])