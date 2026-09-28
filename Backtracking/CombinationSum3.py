class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []
        def backtrack(index,subset,rem):
            if len(subset) == k:
                if rem == 0:
                    ans.append(subset.copy())
                return
            for i in range(index,10):
                subset.append(i)
                backtrack(i+1,subset,rem - i)
                subset.pop()
        backtrack(1,[],n)
        return ans