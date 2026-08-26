class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        hashmap = {0:-1}
        curSum = 0
        for i , n in enumerate(nums):
            curSum+=n
            rem = curSum % k
            if rem in hashmap:
                if i - hashmap[rem] >= 2:
                    return True
            else:
                hashmap[rem] = i
        return False