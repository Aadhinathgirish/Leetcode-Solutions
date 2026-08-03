from collections import deque
class Solution:
    def highestPeak(self, isWater):
        row = len(isWater)
        col = len(isWater[0])
        queue = deque()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False]*col for _ in range(row)]
        newmat = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    newmat[i][j] = 0
                    visited[i][j] = True
                    queue.append((i,j))
        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                newr = r + dr
                newc = c + dc
                if 0 <= newr < row and 0 <= newc < col:
                    if not visited[newr][newc]:
                        newmat[newr][newc] = newmat[r][c] + 1
                        visited[newr][newc] = True
                        queue.append((newr,newc))
        return newmat
