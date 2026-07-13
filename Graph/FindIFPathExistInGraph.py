class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        graph = [[] for _  in range(n)]
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        visited = [False]*n
        def dfs(start,destintion):
            if start == destination:
                return True
            if visited[start]:
                return
            visited[start] = True
            for i in graph[start]:
                if not visited[i]:
                    if dfs(i,destination):
                        return True
            return False
        return dfs(source,destination)

            
        
