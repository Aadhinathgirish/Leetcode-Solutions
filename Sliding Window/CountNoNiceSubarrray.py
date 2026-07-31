class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        def AtmostK(nums,k):
            l = 0
            r = 0
            count = 0
            while r < len(nums):
                if nums[r] % 2 != 0:
                    k-=1
                while k < 0:
                    if nums[l]%2 != 0:
                        k+=1
                    l+=1
                count += r-l-1
                r+=1
            return count
        return AtmostK(nums,k) - AtmostK(nums,k-1)