class Solution:
    def findCenter(self, edges) -> int:
            if edges[0][0] in edges[1]:
                return edges[0][0]
            else:
                return edges[0][1]
        