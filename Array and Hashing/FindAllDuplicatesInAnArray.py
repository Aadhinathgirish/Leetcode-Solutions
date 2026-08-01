class Solution:
    def findDuplicates(self, nums):
        hashmap = {}
        ans = []
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        for i in hashmap:
            if hashmap[i] >= 2:
                ans.append(i)
        return ans