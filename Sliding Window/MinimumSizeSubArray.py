class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        l,r=0,0
        res=len(nums)+1
        output=0
        while r < len(nums):
            output += nums[r]
            while output >= target:
                res = min(res,r-l+1)
                output-= nums[l]
                l+=1
            r+=1
        return res if res!=len(nums)+1 else 0

                

                

        