class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i,n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum > target:
                    r-=1
                else:
                    l+=1
                if abs(curSum-target) < abs(closest-target):
                    closest = curSum
        return closest