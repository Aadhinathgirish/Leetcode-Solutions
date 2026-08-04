from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        queue = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False]*col for _ in range(row)]
        def bfs(i,j):
            queue.append((i,j))
            visited[i][j] = True
            area = 1
            while queue:
                r , c = queue.popleft()
                for dr,dc in directions:
                    newr = r + dr
                    newc = c + dc
                    if 0<=newr<row and 0<=newc<col:
                        if grid[newr][newc] == 1 and not visited[newr][newc]:
                            queue.append((newr,newc))
                            visited[newr][newc] = True
                            area+=1
            return area
        maxarea = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not visited[i][j]:
                    res = bfs(i,j)
                    maxarea = max(res,maxarea)
        return maxarea
