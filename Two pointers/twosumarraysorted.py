class Solution:
    def twoSum(self, number,target: int):
        l = 0
        r = len(number) - 1
        while l < r:
            if number[l] + number[r] == target:
                return [l+1,r+1]
            elif number[l] + number[r] > target:
                r-=1
            else:
                l+=1
            