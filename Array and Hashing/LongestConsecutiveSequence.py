class Solution:
    def longestConsecutive(self, nums) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in nums:
                current = num
                streak = 1
                while current+1 in nums:
                    streak+=1
                    current = current + 1
                ans = max(ans,streak)
        return ans

