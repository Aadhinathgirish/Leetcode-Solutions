class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        MinSum = float('inf')
        MaxSum = float('-inf')
        curMin = float('inf')
        curMax = float('-inf')
        for i in nums:
            curMin = min(i,curMin+i)
            curMax = max(i,curMax+i)
            MaxSum = max(curMax,MaxSum)
            MinSum = min(curMin,MinSum)
        if MaxSum < 0:
            return MaxSum
        else:
            return max(MaxSum,sum(nums)-MinSum)