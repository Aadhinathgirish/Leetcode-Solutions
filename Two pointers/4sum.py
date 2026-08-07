class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        ans = set()
        for j,k in enumerate(nums):
            if j > 0 and k == nums[j-1]:
                continue
            for i in range(j+1,len(nums)):
                l = i+1
                r = len(nums) - 1
                while l < r:
                    curSum = nums[j] + nums[i] + nums[l] + nums[r]
                    if curSum > target:
                        r-=1
                    elif curSum < target:
                        l+=1
                    else:
                        ans.add((nums[j],nums[i],nums[l],nums[r]))
                        l+=1
        return list(ans)
