import traceback
def nameSplitter(name):
    
    head = -1
    number = -1
    
    for i in range(len(name)):
        if name[i] in '0123456789':
            head = i -1
            break
            
    for i in range(head + 1, len(name)):
        if name[i] not in '0123456789':
            number = i - 1
            break
        elif i == len(name) - 1: number = i
    try:
        headStr = name[:head + 1].lower()
        
    except Exception as e:
        print(e)
        headStr = name[:head + 1]
        
    return (headStr, int(name[head + 1: number + 1]))
    
    
def solution(files):
    return sorted(files, key=nameSplitter)