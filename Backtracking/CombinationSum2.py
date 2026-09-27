class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans = []
        def backtrack(index,subset,rem):
            if rem == 0:
                ans.append(subset.copy())
                return
            if rem < 0:
                return
            if len(candidates) == index:
                return
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                backtrack(i+1,subset,rem-candidates[i])
                subset.pop()
        backtrack(0,[],target)
        return ans