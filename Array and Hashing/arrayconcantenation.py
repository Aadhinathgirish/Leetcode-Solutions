def arrcon(nums,x):
    ans=[]
    for i in range(x):
        for n in nums:
            ans.append(n)
        i+=1
    return ans


print(arrcon([1,2,3],2))