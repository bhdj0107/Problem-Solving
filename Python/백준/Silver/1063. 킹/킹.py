import sys
from collections import deque

mapper = 'ABCDEFGH'
mapper = {i:ord(i)-ord('A') for i in mapper}

def moveTransform(move):
    ret = [0, 0]
    movesMap = {
        "T": (1, 0),
        "B": (-1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }
    for c in move:
        ret = [sum(i) for i in zip(ret, movesMap[c])]
    return ret

king, stone, moves = sys.stdin.readline().split()
king = tuple((int(king[1]) - 1, mapper[king[0]]))
stone = (int(stone[1]) - 1, mapper[stone[0]])
moves = int(moves)
moves = [sys.stdin.readline().rstrip() for _ in range(moves)]
moves = list(map(moveTransform, moves))


def moveKing(move, king, stone):
    newKing = tuple((sum(i) for i in zip(king, move)))
    if sum([newKing[i] < 0 or newKing[i] >= 8 for i in range(2)]) > 0: return ((-3, -3), (-3, -3))
    else:
        if stone == newKing:
            newStone = tuple((sum(i) for i in zip(stone, move)))
            if sum([newStone[i] < 0 or newStone[i] >= 8 for i in range(2)]) > 0: return ((-3, -3), (-3, -3))
            else:
                return (newKing, newStone)
        else:
            return (newKing, stone)    


for move in moves:
    newKing, newStone = moveKing(move, king, stone)
    if newKing == (-3, -3): continue
    else:
        king = newKing
        stone = newStone


print(f'{chr(ord("A") + king[1])}{king[0] + 1}')
print(f'{chr(ord("A") + stone[1])}{stone[0] + 1}')