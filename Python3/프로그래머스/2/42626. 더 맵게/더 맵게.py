import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    scov = scoville
    answer = 0
    while True:
        sco = heapq.heappop(scov)
        if sco < K:
            if not scov: return -1
            sco2 = heapq.heappop(scov)
            answer += 1
            heapq.heappush(scov, sco + (sco2 * 2))
        else: break

    
    return answer