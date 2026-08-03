from collections import deque
class Solution:
    def nearestExit(self, maze, entrance) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        shortest = 0
        col = len(maze[0])
        row = len(maze)
        visited = [[False]*col for _ in range(row)]
        queue.append((entrance[0],entrance[1]))
        visited[entrance[0]][entrance[1]] = True
        entrance = tuple(entrance)
        while queue:
            Qlen = len(queue)
            change = False
            for i in range(Qlen):
                r,c = queue.popleft()
                if (r==0 or r== row -1 or c == 0 or c == col-1) and (r,c) != entrance:
                    return shortest
                for dr , dc in directions:
                        newr = r + dr
                        newc = c + dc
                        if 0 <= newr < row and 0 <= newc < col:
                            if not visited[newr][newc]:
                                if maze[newr][newc] == '.':
                                    change = True
                                    queue.append((newr,newc))
                                    visited[newr][newc] = True
            if change:
                shortest+=1
            else:
                return -1
        return shortest