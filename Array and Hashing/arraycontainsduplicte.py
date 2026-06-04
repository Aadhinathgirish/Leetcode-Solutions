def condupli(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

print(condupli([1,2,3,4,1,6]))
            