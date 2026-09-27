class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def backtrack(index,subset):

            if index == len(nums):
                ans.append(subset.copy())
                return
            subset.append(nums[index])
            backtrack(index+1,subset)
            subset.pop()
            backtrack(index+1,subset)
        backtrack(0,[])
        return ans