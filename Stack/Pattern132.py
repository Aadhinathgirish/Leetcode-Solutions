class Solution:
    def find132pattern(self, nums) -> bool:
        second = float('-inf')
        stack = []
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] < nums[i]:
                ans = stack.pop()
                second = ans
            if second > nums[i]:
                return True
            stack.append(nums[i])
        return False