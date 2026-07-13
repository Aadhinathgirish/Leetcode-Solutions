class Solution:
    def findCircleNum(self, isConnected) -> int:
        visited = [False]*len(isConnected)
        n = len(isConnected)
        p = 0
        def dfs(city):
            if visited[city]:
                return
            visited[city] = True
            for i in range(n):
                if isConnected[city][i] == 1 and not visited[i]:
                    dfs(i)
        for i in range(n):
            if not visited[i]:
                p+=1
                dfs(i)
        return p