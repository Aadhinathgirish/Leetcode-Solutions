from collections import deque
class Solution:
    def islandPerimeter(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        visited = [[False]*col for _ in range(row)]
        def bfs(i,j):
            queue.append((i,j))
            Total_peri = 0
            visited[i][j] = True
            while queue:
                r,c = queue.popleft()
                perimeter = 4
                for dr , dc in directions:
                    newr = r + dr
                    newc = c + dc
                    if 0 <= newr < row and 0 <= newc < col:
                        if not visited[newr][newc] and grid[newr][newc] == 1:
                            visited[newr][newc] = True
                            queue.append((newr,newc))
                        if grid[newr][newc] == 1:
                            perimeter -=1
                Total_peri += perimeter
            return Total_peri
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return bfs(i,j)
