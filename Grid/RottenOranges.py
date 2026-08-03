from collections import deque
class Solution:
    def orangesRotting(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False] * col for _ in range(row)]
        queue = deque()
        minutes = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited[i][j] = True
        while queue:
            Qlen = len(queue)
            change = False
            for i in range(Qlen):
                r,c = queue.popleft()
                for dr,dc in directions:
                    newr = r + dr
                    newc = c + dc
                    if 0 <= newr < row and 0 <= newc < col:
                        if not visited[newr][newc]:
                            if grid[newr][newc] == 1:
                                change = True
                                visited[newr][newc] = True
                                grid[newr][newc] = 2
                                queue.append((newr,newc))
            if change:
                minutes+=1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return minutes

                    
            