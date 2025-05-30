def solve_probs(diffs, times, level):
    total = 0
    for i, diff in diffs.items():
        if i == 0: continue
        repeat = diff - level
        if repeat > 0:
            total += repeat * (times[i] + times[i - 1])
        total += times[i]
            
    return total

def solution(diffs, times, limit):
    diffs = {i + 1:diffs[i] for i in range(len(diffs))}
    diffs[0] = 0
    
    times = {i + 1:times[i] for i in range(len(times))}
    times[0] = 1
    

    answer = 0
    
    # 이분탐색
    left = 0
    right = 100000
    
    while True:
        if left + 1 == right: break
        
        middle = (left + right) // 2
        
        used_time = solve_probs(diffs, times, middle)
        if used_time > limit: left = middle
        else: right = middle
    
    return right