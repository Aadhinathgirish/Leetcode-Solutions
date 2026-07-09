class Solution:
    def minOperations(self, nums) -> int:
        l = 0
        r = 2
        operations = 0
        while l<= len(nums)-3:
            if nums[l] == 0:
                nums[l] = 1
                if nums[l+1] == 0:
                    nums[l+1] =1
                else:
                    nums[l+1] = 0
                if nums[r] == 0:
                    nums[r] = 1
                else:
                    nums[r] = 0
                operations+=1
            l+=1
            r+=1
        
        return -1 if 0 in nums else operations
            
            

        
        