import sys
import heapq
input = sys.stdin.readline

class DoublePriorityQueue:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.item_map = {}
        self.total_item = 0 
    
    def push(self, item):
        heapq.heappush(self.maxheap, -item)
        heapq.heappush(self.minheap, item)
        if item in self.item_map.keys(): self.item_map[item] += 1
        else: self.item_map[item] = 1
        self.total_item += 1
        
    def pop(self, D):
        if not self.total_item: return None
        while True:
            popped = -D * heapq.heappop(self.maxheap if D == 1 else self.minheap)
            if self.item_map.get(popped):
                self.item_map[popped] -= 1
                if self.item_map[popped] == 0:
                    del self.item_map[popped]
                self.total_item -= 1
                if self.total_item == 0:
                    self.maxheap = []
                    self.minheap = []               
                return popped


    
T = int(input())
for _ in range(T):
    N = int(input())
    dHeap = DoublePriorityQueue()
    for _ in range(N):
        op, item = input().split()
        item = int(item)
        if op == 'I': dHeap.push(item)
        else: dHeap.pop(item)
    
    if dHeap.total_item >= 2:
        a, b = dHeap.pop(1), dHeap.pop(-1)
        print(a, b)
    elif dHeap.total_item == 1:
        for k in dHeap.item_map.keys():
            print(k, k)
    else:
        print("EMPTY")