class Solution:
    def jump(self, nums) -> int:
        if len(nums) == 1:
            return 0
        farthest = 0
        currentend = 0
        jump = 0
        for i in range(len(nums)):
            if currentend == len(nums)-1:
                return jump
            farthest = max(farthest,i+nums[i])
            if i == currentend:
                jump+=1
                currentend = farthest
        return jump