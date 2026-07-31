class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        nums.sort()
        l = 0
        r = 0
        maxlen = 0
        windowSum = 0
        while r < len(nums):
            windowSum += nums[r]
            while ((r-l+1) * nums[r] - windowSum) > k:
                windowSum -= nums[l]
                l+=1
            maxlen = max(maxlen,r-l+1)
            r+=1
        return maxlen