def removeelement(nums,value):
    k=0
    for i in range(len(nums)):
        if nums[i]!=value:
            nums[k]=nums[i]
            k+=1
    return k,nums

print(removeelement([3,2,2,3],3))