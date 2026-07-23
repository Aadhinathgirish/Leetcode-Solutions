class Solution:
    def splitArray(self, nums, k: int) -> int:

        def possible(mid,k,nums):
            pages = 0
            a  =  1
            for i in range(len(nums)):
                pages += nums[i]
                if pages > mid:
                    a +=1
                    pages = nums[i]
            return a <= k
        
        l = max(nums)
        r = sum(nums)
        ans = 0
        while l <= r:
            mid = l + (r-l)//2
            if possible(mid,k,nums):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans if ans else 0