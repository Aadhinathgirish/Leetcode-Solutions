class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        start  = 0
        stack = [start]
        visited = [False]*len(rooms)
        while stack:
            cur = stack.pop()
            if not visited[cur]:
                visited[cur] = True
                for i in rooms[cur]:
                    if not visited[i]:
                        stack.append(i)
        return True if False not in visited else False