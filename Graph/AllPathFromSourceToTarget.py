class Solution:
    def allPathsSourceTarget(self, graph):
        path = []
        res = []
        def dfs(start):
            path.append(start)
            if start == len(graph)-1:
                res.append(list(graph))
            else:
                for i in graph[start]:
                    if i not in path:
                        dfs(i)
            path.pop()
        dfs(0)
        return res