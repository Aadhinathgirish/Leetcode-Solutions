class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        def backtrack(index,subset,rem):
            if rem == 0:
                ans.append(subset.copy())
                return
            if rem < 0:
                return
            if index == len(candidates):
                return
            subset.append(candidates[index])
            backtrack(index,subset,rem-candidates[index])
            subset.pop()
            backtrack(index+1,subset,rem)
        backtrack(0,[],target)
        return ans
