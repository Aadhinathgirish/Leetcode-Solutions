class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        row = len(grid)
        column = len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=column or grid[r][c] =='0':
                return
            grid[r][c] = '0'
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        count = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count+=1
        return count
            


        
