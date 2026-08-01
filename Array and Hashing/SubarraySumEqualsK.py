class Solution:
    def subarraySum(self, nums, k: int) -> int:
        count = {0:1}
        currentSum = 0
        ans = 0
        for i in nums:
            currentSum += i
            if (currentSum - k) in count:
                ans+= count[currentSum - k]
            count[currentSum] = 1 + count.get(currentSum,0)
        return ans
        
       
            