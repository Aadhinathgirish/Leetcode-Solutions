class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        maxValue = float('-inf')
        l = 0
        r = 0
        ans = 0
        while r < len(nums):
            ans+=nums[r]
            if r - l + 1 > k:
                ans-=nums[l]
                l+=1
            if r - l +1 == k:
                maxValue = max(maxValue,ans/k)
            r+=1
        return maxValue