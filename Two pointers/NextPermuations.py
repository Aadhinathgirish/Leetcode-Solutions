class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        pivot = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                pivot = nums[i]
                index = i
                break
        if pivot == -1:
            return nums.sort()

        minval = nums[index+1]
        newindex = index+1
        for i in range(index+1,len(nums)):
            if nums[i] < minval and nums[i] > pivot:
                minval = nums[i]
                newindex = i
        nums[index],nums[newindex] = nums[newindex],nums[index]
        nums[index+1:] = sorted(nums[index+1:])
    
        
    

        
        