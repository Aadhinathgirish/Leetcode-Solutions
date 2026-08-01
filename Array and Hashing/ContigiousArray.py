class Solution:
    def findMaxLength(self, nums) -> int:
        for i in range(len(nums)):
            if nums[i] ==0:
                nums[i] = -1
        hashmap = {0:-1}
        ans = 0
        length = 0
        for i in range(len(nums)):
            ans+= nums[i]
            if ans in hashmap:
                length = max(length,i-hashmap[ans])
            else:
                hashmap[ans] = i
        return length
                