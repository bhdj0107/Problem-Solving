import sys
class Q:
    def __init__(self):
        self.container = {}
        self.head = 0
    def __len__(self):
        return len(self.container)
    def append(self, n):
        self.container[len(self) + self.head] = n
    def pop(self):
        if len(self):
            tmp = self.container[self.head]
            del self.container[self.head]
            self.head += 1
            return tmp
        else:
            raise Exception('빈 큐 에러')
            return None

T = int(sys.stdin.readline())
for _ in range(T):
    q = Q()
    p_cnt = [0 for _ in range(9)]
    cnt = 0
    N, ans = map(int, sys.stdin.readline().split())
    prior = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        q.append((i, prior[i]))
        p_cnt[prior[i] - 1] += 1
    for i in range(8, -1, -1):
        while p_cnt[i]:
            tmp = q.pop()
            if tmp[1] == i + 1:
                if tmp[0] == ans:
                    print(cnt + 1)
                    p_cnt[i] -= 1
                else:
                    cnt += 1
                    p_cnt[i] -= 1
            else:
                q.append(tmp)
                
        