from collections import deque
class Solution:
    def updateMatrix(self, mat):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        row = len(mat)
        col = len(mat[0])
        queue = deque()
        visited = [[False] * col for _ in range(row)]
        newmat = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    newmat[i][j] == 0
                    queue.append((i,j))
                    visited[i][j] = True
        while queue:
            r,c = queue.popleft()
            for dr , dc in directions:
                newr = r + dr
                newc = c + dc
                if 0<=newr<row and 0<=newc<col:
                    if not visited[newr][newc]:
                        newmat[newr][newc] = newmat[r][c] + 1
                        queue.append((newr,newc))
                        visited[newr][newc] = True
        return newmat
