class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        nums.sort()
        l = 0
        r = 0
        minVal = max(nums)
        while r < len(nums):
            if r - l + 1 > k:
                l +=1
            if r - l +1 == k:
                minVal = min(minVal,abs(nums[r]-nums[l]))
            r+=1
        return minVal