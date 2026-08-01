class Solution:
    def findNumbers(self, nums) -> int:
        count = 0
        for i in nums:
            j = 0
            while i > 0:
                i = i // 10
                j+=1
            if j%2 == 0:
                count+=1  
        return count