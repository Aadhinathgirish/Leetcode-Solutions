class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rowhash = {}
        colhash = {}
        n = len(grid)
        count = 0
        for i in range(n):
            ans = []
            for j in range(n):
                ans.append(grid[i][j])
            rowhash[tuple(ans)] = 1 + rowhash.get(tuple(ans),0)
        for i in range(n):
            ans = []
            for j in range(n):
                ans.append(grid[j][i])
            colhash[tuple(ans)] = 1 + colhash.get(tuple(ans),0)
        for i in rowhash:
            if i in colhash:
                count += rowhash[i] * colhash[i]
        return count
        