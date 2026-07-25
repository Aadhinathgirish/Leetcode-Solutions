class Solution:
    def maximumSubarraySum(self, nums, k: int) -> int:
        l = 0
        r = 0
        maxSum = 0
        count = {}
        ans = 0
        while r < len(nums):
            count[nums[r]] = 1 + count.get(nums[r],0)
            ans += nums[r] 
            if r - l + 1 == k:
                if len(count) == k:
                    maxSum = max(ans,maxSum)
                ans -= nums[l]
                count[nums[l]] -=1
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                l +=1
            r+=1
        return maxSum

