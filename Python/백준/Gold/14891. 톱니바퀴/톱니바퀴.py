import sys
import math
class Cog:
    def __init__(self, status,):
        self.status = list(status)
        self.top = 0
    
    def rotate(self, direction):
        self.top += 8 - direction
        self.top %= 8

    def getTop(self):
        return self.status[self.top]

    def getLeft(self):
        return self.status[(self.top + 6) % 8]

    def getRight(self):
        return self.status[(self.top + 2) % 8]
    
class CogSet:
    def __init__(self, statuses):
        self.cogs = [Cog(status) for status in statuses]

    def rotate(self, cognum, direction):
        cognum -= 1
        lefts = [cog.getLeft() for cog in self.cogs]
        rights = [cog.getRight() for cog in self.cogs]

        rotateCogs = [(cognum, direction)]
        for i in range(cognum):
            if rights[cognum - i - 1] != lefts[cognum - i]:
                if i % 2 == 0: newDirection = direction * -1
                else: newDirection = direction
                rotateCogs.append((cognum - i - 1, newDirection))
            else: break

        for i in range(3 - cognum):
            if lefts[cognum + i + 1] != rights[cognum + i]:
                if i % 2 == 0: newDirection = direction * -1
                else: newDirection = direction
                rotateCogs.append((cognum + i + 1, newDirection))
            else: break
        for cogNum, direction in rotateCogs:
            self.cogs[cogNum].rotate(direction)

    def getScore(self):
        total = 0
        for i in range(4):
            total += int(self.cogs[i].getTop()) * int(math.pow(2, i))
        return total

statuses = [sys.stdin.readline() for _ in range(4)]

cogset = CogSet(statuses)
N = int(sys.stdin.readline())
for _ in range(N):
    cognum, direction = map(int, sys.stdin.readline().split())
    cogset.rotate(cognum, direction)

print(cogset.getScore())