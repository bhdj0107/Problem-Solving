from collections import deque
inf = 99999

class Block:
    def setShape(self, mins, maxs, blockPts, startPt):
        min_y, min_x = mins
        max_y, max_x = maxs
        self.height = max_y - min_y + 1
        self.width = max_x - min_x + 1
        self.block = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.size = len(blockPts)
        for pt in blockPts:
            y = pt[0] - min_y
            x = pt[1] - min_x
            self.block[y][x] = 1
        self.rotateHasher = {}
                   
    def isSame(self, block):
        if self.size != block.size: return False
        for r in range(4):
            rBlock = block.getRotated(r)
            if (self.height, self.width) == (rBlock.height, rBlock.width):
                compare = sum([sum([self.block[i][j] != rBlock.block[i][j] for j in range(self.width)]) for i in range(self.height)])
                if not compare: return True
        return False
                            
    def getRotated(self, deg):
        deg = (4 + deg) % 4
        if deg != 0:
            newBlock = Block()
        else: newBlock = self
        if self.rotateHasher.get(deg):
            return self.rotateHasher[deg]
        if deg == 1:
            newBlock.height = self.width
            newBlock.width = self.height
            newBlock.block = [[0 for _ in range(newBlock.width)] for _ in range(newBlock.height)]
            newBlock.size = self.size
            for i in range(self.height):
                for j in range(self.width):
                    newBlock.block[j][self.height - i - 1] = self.block[i][j]
        elif deg == 2:
            newBlock.height = self.height
            newBlock.width = self.width
            newBlock.block = [[0 for _ in range(newBlock.width)] for _ in range(newBlock.height)]
            newBlock.size = self.size
            for i in range(self.height):
                for j in range(self.width):
                    newBlock.block[self.height - i - 1][self.width - j - 1] = self.block[i][j]   
                    
        elif deg == 3:
            newBlock.height = self.width
            newBlock.width = self.height
            newBlock.block = [[0 for _ in range(newBlock.width)] for _ in range(newBlock.height)]
            newBlock.size = self.size
            for i in range(self.height):
                for j in range(self.width):
                    newBlock.block[self.width - j - 1][i] = self.block[i][j]
        self.rotateHasher[deg] = newBlock
        return newBlock

class InBoardChecker:
    def __init__(self, game_board):
        self.height, self.width = len(game_board), len(game_board)
    def check(self, pt):
        return not(pt[0] < 0 or pt[0] >= self.height or pt[1] < 0 or pt[1] >= self.width)


def getBlocksFromField(field, status):
    blocks = []
    d = ((0, 1), (1, 0), (0, -1), (-1, 0))
    checker = InBoardChecker(field)
    tableVisited = set()
    # Block Loop
    for i in range(len(field)):
        for j in range(len(field)):
            if (i, j) in tableVisited: continue
            if field[i][j] == status:
                startpt = (i, j)
                q = deque()
                q.append((i, j))
                visited = set()
                min_y, min_x = inf, inf
                max_y, max_x = -inf, -inf
                
                # get block
                while q:
                    pt = q.popleft()
                    if pt in visited: continue
                    else:
                        visited.add(pt)
                        tableVisited.add(pt)
                        min_y = min(min_y, pt[0])
                        min_x = min(min_x, pt[1])
                        
                        max_y = max(max_y, pt[0])
                        max_x = max(max_x, pt[1])
                        
                        for di in range(4):
                            ny, nx = pt[0] + d[di][0], pt[1] + d[di][1]
                            if checker.check((ny, nx)) and field[ny][nx] == status:
                                q.append((ny, nx))
                
                # build block
                newBlock = Block()
                newBlock.setShape((min_y, min_x), (max_y, max_x), visited, startpt)
                blocks.append(newBlock)
    return blocks

        
def solution(game_board, table):
    global boardBlockLen, blockFit
    boardBlocks = getBlocksFromField(game_board, 0)
    tableBlocks = getBlocksFromField(table, 1)
    
    answer = 0
    filled = [False for _ in range(len(boardBlocks))]
    for tBIdx, tb in enumerate(tableBlocks):
        for bBIdx, bb in enumerate(boardBlocks):
            if filled[bBIdx]: continue
            if tb.isSame(bb):
                answer += tb.size
                filled[bBIdx] = tBIdx + 1
                break
    
    return answer
