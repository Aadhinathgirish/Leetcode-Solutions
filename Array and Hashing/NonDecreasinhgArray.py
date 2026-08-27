class Solution:
    def checkPossibility(self, nums) -> bool:
        k = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if k > 0:
                    k-=1
                    if i== 0 or nums[i+1] >= nums[i-1]:
                        nums[i] = nums[i+1]
                    else:
                        nums[i+1] = nums[i]
                else:
                    return False
        return True