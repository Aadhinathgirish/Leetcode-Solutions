def majority(num):
    res={}
    for i in num:
        res[i] = 1 + res.get(i,0) 
    for j in res:
        if res[j] > (len(num)/2):
            return j
    return j
    

print(majority([5,1,1,1,5,4,1]))