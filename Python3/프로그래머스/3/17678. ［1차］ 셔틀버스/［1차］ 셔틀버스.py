from datetime import datetime, timedelta
from collections import deque
class Bus:
    def __init__(self, startTime, waitDuration, capacity):
        self.startTime = startTime
        self.waitDuration = waitDuration
        self.capacity = capacity
        
    def canTakable(self, passenger):
        return passenger <= self.startTime
    
    
        

        
def solution(n, t, m, timetable):
    start = datetime(year=2000, month=1, day=1, hour=9)
    duration = timedelta(minutes=t)
    capacity = m
    
    buses = [Bus(start + duration * i, duration, capacity) for i in range(n)]
    passengers = []
    tempTime = datetime(year=2000, month=1, day=1)
    for t in timetable:
        hour, minute = map(int, t.split(":"))
        tempDelta =  timedelta(hours=hour, minutes=minute)
        passengers.append(tempTime + tempDelta)
    passengers.sort()
    passengers = deque(passengers)
    
    # 마지막 버스 제외 하고 승객 태워가기
    for bus in buses[:-1]:
        for _ in range(bus.capacity):
            if passengers:
                if bus.canTakable(passengers[0]):
                    passengers.popleft()
    
    # 마지막 버스
    lastBus = buses[-1]
    latest = datetime(year=1999, month=1, day=1)
    for _ in range(lastBus.capacity):
        if passengers:
            if lastBus.canTakable(passengers[0]):
                took = passengers.popleft()
                lastBus.capacity -= 1
                if took > latest:
                    latest = took
    answer = ""         
    if lastBus.capacity == 0:
        answer = (latest - timedelta(minutes=1)).strftime("%H:%M")
    else:
        answer = lastBus.startTime.strftime("%H:%M")
    return answer