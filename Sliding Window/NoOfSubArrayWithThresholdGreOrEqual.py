class Solution:
    def numOfSubarrays(self, nums, k: int, threshold: int) -> int:
        l = 0
        r = 0
        count = 0
        ans = 0
        while r < len(nums):
            ans += nums[r]
            if r - l + 1 > k:
                ans -= nums[l]
                l+=1
            if r-l+1 == k:
                if ans//k >= threshold:
                    count+=1
            r+=1
        return count