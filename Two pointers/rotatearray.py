def rotatearray(nums,k):
     k = k%len(nums)
     def helper(l,r,nums):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l = l+1
                r = r-1
            helper(0,k-1,nums)
            helper(k,len(nums)-1,nums)
            return
     helper(0,len(nums)-1,nums)
     return  nums    
print(rotatearray([1,2,3,4,5,6,7,8],4))      
    