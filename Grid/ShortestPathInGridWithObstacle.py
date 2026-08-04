from collections import deque
class Solution:
    def shortestPath(self, grid, k: int) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        row = len(grid)
        col = len(grid[0])
        visited = set()
        queue.append((0,0,k))
        visited.add((0,0,k))
        shortest = 0
        while queue:
            Qlen = len(queue)
            for i in range(Qlen):
                r,c,n = queue.popleft()
                if r == row-1 and c == col -1:
                    return shortest
                for dr , dc in directions:
                        newr = r + dr
                        newc = c + dc
                        if 0 <= newr < row and 0 <= newc < col:
                            if (newr,newc,n) not in visited and grid[newr][newc] == 0:
                                queue.append((newr,newc,n))
                                visited.add((newr,newc,n))
                            if (newr,newc,n-1) not in visited and grid[newr][newc] == 1 and n > 0:
                                queue.append((newr,newc,n-1))
                                visited.add((newr,newc,n-1))
            shortest+=1  
        return -1     




                        

