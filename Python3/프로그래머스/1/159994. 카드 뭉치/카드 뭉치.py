from collections import deque
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    c1 = cards1.popleft()
    c2 = cards2.popleft()
    for _ in range(len(goal)):
        g = goal.popleft()
        if c1 == g: 
            if cards1: c1 = cards1.popleft()
            else: c1 = ""
        elif c2 == g: 
            if cards2: c2 = cards2.popleft()
            else: c2 = ""
        else: return "No"
    return "Yes"