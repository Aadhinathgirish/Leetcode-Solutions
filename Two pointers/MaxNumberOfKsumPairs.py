class Solution:
    def maxOperations(self, nums, k: int) -> int:
        l = 0
        r = len(nums)-1
        nums.sort()
        op=0
        while l < r:
            if nums[l] + nums[r] == k:
                op+=1
                l+=1
                r-=1
            elif nums[l] + nums[r] < k:
                l+=1
            else:
                r-=1
        return op