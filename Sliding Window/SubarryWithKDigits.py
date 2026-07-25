class Solution:
    def subarraysWithKDistinct(self, nums, k: int) -> int:
        def kDigits(nums,k):
            count = {}
            l = 0
            res = 0
            r = 0
            while r < len(nums):
                count[nums[r]] = 1 + count.get(nums[r],0)
                while len(count)>k:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        count.pop(nums[l])
                    l+=1
                res+=(r-l)+1
                r += 1
            return res
        return kDigits(nums,k) - kDigits(nums,k-1)