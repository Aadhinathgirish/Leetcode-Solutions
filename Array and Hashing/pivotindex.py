class Solution:
    def pivotIndex(self, nums) -> int:
        sumleft = 0
        total = sum(nums)
        for i in range(len(nums)):
            sumright = total - sumleft - nums[i]
            if sumleft == sumright:
                return i
            sumleft = sumleft + nums[i]
        return -1
