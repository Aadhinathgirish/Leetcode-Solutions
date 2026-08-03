from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        queue = deque()
        shortest = 0
        col , row = len(grid[0]) ,len(grid)
        visited = [[False]*col for _ in range(row)]
        if grid[row -1][col-1] == 1:
            return -1
        if grid[0][0] == 0:
            visited[0][0] = True
            shortest+=1
            queue.append((0,0))
        else:
            return -1
        while queue:
            Qlen = len(queue)
            change = False
            for i in range(Qlen):
                r,c = queue.popleft()
                if r == row-1 and c == col-1:
                    return shortest
                for dr , dc in directions:
                    newr = r + dr
                    newc = c + dc
                    if 0 <= newr < row and 0 <= newc < col:
                        if not visited[newr][newc]:
                            if grid[newr][newc] == 0:
                                queue.append((newr,newc))
                                visited[newr][newc] = True
                                change = True
            if change:
                shortest +=1
            else:
                return -1
        return shortest
                    

