import sys
class deque:
    def __init__(self):
        self.container = {}
        self.head = 0
        self.tail = 0
    def __len__(self):
        return len(self.container)
    def append(self, n):
        self.container[self.tail] = n
        self.tail += 1
    def appendleft(self, n):
        self.head -= 1
        self.container[self.head] = n
    def pop(self):
        if len(self):
            self.tail -= 1
            tmp = self.container[self.tail]
            del self.container[self.tail]
            return tmp
        else:
            return -1
    def popleft(self):
        if len(self):
            tmp = self.container[self.head]
            del self.container[self.head]
            self.head += 1
            return tmp
        else:
            return -1
    def value(self, n):
        if len(self):
            return self.container[self.head + n]
        else:
            return -1

dq = deque()
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    inp = list(map(str, (input().rstrip() + ' 0').split()))
    if inp[0] == 'push_front':
        dq.appendleft(inp[1])
    elif inp[0] == 'push_back':
        dq.append(inp[1])
    elif inp[0] == 'pop_front':
        print(dq.popleft())
    elif inp[0] == 'pop_back':
        print(dq.pop())
    elif inp[0] == 'empty':
        print(int(not bool(len(dq))))
    elif inp[0] == 'size':
        print(len(dq))
    elif inp[0] == 'front':
        print(dq.value(0))
    elif inp[0] == 'back':
        print(dq.value(len(dq) - 1))