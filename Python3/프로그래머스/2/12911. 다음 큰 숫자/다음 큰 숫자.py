from collections import deque
def solution(n):
    counter = [-1, -1]
    
    switchCount = 0
    
    binN = deque('0' + bin(n)[2:] + '0')
    now = '0'
    while switchCount < 2:
        rightest = binN.pop()
        if rightest != now: 
            switchCount += 1
            now = rightest
        counter[int(rightest)] += 1
    

    zeros = '0' * counter[0]
    ones = '1' * counter[1]
    
    if binN: answer = int('0b' + ''.join(binN) + '1', 2) 
    else: answer = 1
    answer = (answer * (2 ** sum(counter))) + (2 ** counter[1] - 1)
    return answer
