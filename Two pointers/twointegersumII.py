def twosum(nums,target):
    for i,n in enumerate(nums,1):
        l,r = 0,len(nums)-1
        while l < r:
            curSum = nums[l]+nums[r]
            if curSum > target:
                r-=1
            elif curSum < target:
                l+=1
            else:
                return [l+1,r+1]

print(twosum([1,4,6,7,8,9],13))