import collections
class Solution:
    def maxSlidingWindow(self, nums, k: int) -> :
        l=0
        r=0
        queue = collections.deque()
        output = []
        while r<len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            if l > queue[0]:
                queue.popleft()
            if r-l+1 >= k:
                output.append(nums[queue[0]])
                l+=1
            r+=1
        return output
