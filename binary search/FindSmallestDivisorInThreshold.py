from math import ceil
class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        def thres(nums,threshold,val):
            res = 0
            for i in nums:
                ans = ceil(i/val)
                res += ans
            return res<=threshold

        l = 1
        r = max(nums)
        output = 0
        while l <= r:
            mid = l + ((r-l))//2
            if thres(nums,threshold,mid):
                output = mid
                r = mid-1
            else:
                l = mid+1
        return output

