def twosum(num,target):
    newhash ={}
    for i,num in enumerate(num):
        diff = target - num
        if diff in newhash:
            return [i,newhash[diff]]
        newhash[num] = i

print(twosum([4,2,7,8,4],10))