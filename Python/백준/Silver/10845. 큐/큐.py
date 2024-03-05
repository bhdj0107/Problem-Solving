import sys
class queue:
    def __init__(self):
        self.container = ['']
        self.head = 0
    def __len__(self):
        return len(self.container) - self.head - 1
    def pop(self):
        self.head += 1
        return self.container[self.head]
    def push(self, n):
        self.container.append(n)
    def value(self, n):
        if len(self) == 0:
            return -1
        if n >= 0:
            return self.container[self.head + n + 1]
        else:
            return self.container[n]
    
file = queue()
N = int(sys.stdin.readline())
for _ in range(N):
    inp = tuple(map(str, (sys.stdin.readline().rstrip() + " 1").split()))
    if inp[0] == 'push':
        file.push(int(inp[1]))
    elif inp[0] == 'front':
        print(file.value(0))
    elif inp[0] == 'back':
        print(file.value(-1))
    elif inp[0] == 'empty':
        print(int(not bool(len(file))))
    elif inp[0] == 'size':
        print(len(file))
    elif inp[0] == 'pop':
        if len(file):
            print(file.pop())
        else:
            print(-1)
        
        
    