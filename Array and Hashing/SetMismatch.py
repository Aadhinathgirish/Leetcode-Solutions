class Solution:
    def findErrorNums(self, nums):
        count = {}
        ans = []
        n = len(nums)+1
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for i in count:
            if count[i] > 1:
                ans.append(i)
        nums = set(nums)
        for i in range(1,n):
            if i not in nums:
                ans.append(i)
                return ans
        