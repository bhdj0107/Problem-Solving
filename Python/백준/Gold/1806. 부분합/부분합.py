import sys

N, S = map(int, sys.stdin.readline().split())
nums = tuple(map(int, sys.stdin.readline().split()))


answer = 100001
windowTotal = nums[0] 
windowSize = 1

left = 0
right = 0

while True:
    # 윈도우의 총합이 S 보다 이상이라면
    if windowTotal >= S:
        # 윈도우의 길이가 1 이라면 break
        if windowSize == 1:
            answer = 1
            break
        
        # 윈도우의 길이가 2 이상이라면
        else:
            # 현재 윈도우 길이를 정답과 min 도치하고
            answer = min(answer, windowSize)
            
            # left를 오른쪽으로 한 칸 옮긴다
            windowTotal -= nums[left]
            windowSize -= 1
            left += 1
            
    # 윈도우의 총합이 S 미만이라면
    else:
        # right 가 가장 오른쪽이라면
        if right == N - 1: break
        # 아니라면
        else:
            right += 1
            windowTotal += nums[right]
            windowSize += 1
            
print(answer if answer != 100001 else 0)