class Solution:
    def longestSubarray(self, nums) -> int:
        l = 0
        r = 0
        k = 1
        maxlen = 0
        while r < len(nums):
            if nums[r] == 0:
                k-=1
            while k < 0:
                if nums[l] == 0:
                    k+=1                
                l+=1
            maxlen = max(maxlen,r-l)
            r+=1
        return maxlen