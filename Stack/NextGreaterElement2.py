class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        ans = []
        ans = [-1]*(len(nums))
        for i in range(2*len(nums)-1,-1,-1):
            a = i%len(nums)
            while stack and stack[-1] <= nums[a]:
                stack.pop()
            if stack:
                ans[a] = stack[-1]
            stack.append(nums[a])
        return ans

