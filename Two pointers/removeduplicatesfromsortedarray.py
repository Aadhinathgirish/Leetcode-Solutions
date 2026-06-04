def dupli(nums):    
    k = 1
    i = 0
    while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                i+=1
            else:
                nums[k]=nums[i+1]
                k+=1
                i+=1
    return k,nums
print(dupli([0,0,1,1,1,2,2,3,3,4]))