class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def backtrack(i,currentxor):
            if i == len(nums):
                return currentxor
            take = backtrack(i+1,currentxor ^ nums[i])
            skip = backtrack(i+1,currentxor)
            return take + skip
        return backtrack(0,0)