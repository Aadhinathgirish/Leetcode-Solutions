class Solution:
    def findDisappearedNumbers(self, nums):
        ans = []
        n = len(nums) + 1
        nums = set(nums)
        for i in range(1,n):
            if i not in nums:
                ans.append(i)
        return ans