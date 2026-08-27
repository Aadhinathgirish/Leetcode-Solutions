class Solution:
    def summaryRanges(self, nums):
        r = 0
        output = []
        while r < len(nums):
            if nums[r] + 1 in nums:
                current = nums[r]
                while nums[r] + 1 in nums:
                    r+=1
                output.append(f'{current}->{nums[r]}')
            else:
                output.append(str(nums[r]))
            r+=1
        return output