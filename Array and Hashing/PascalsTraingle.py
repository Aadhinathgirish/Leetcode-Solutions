class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = []
        for i in range(numRows):
            row = [0] * (i+1)
            for j in range(i+1):
                if j == 0 or j == i:
                    row[j] = 1
                else:
                    row[j]= ans[i-1][j] + ans[i-1][j-1]
            ans.append(row)
        return ans
                