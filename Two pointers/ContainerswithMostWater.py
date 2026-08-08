class Solution:
    def maxArea(self, height) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l < r:
            area = (r-l) * min(height[r],height[l])
            maxArea = max(maxArea,area)
            if height[r] < height[l]:
                r-=1
            else:
                l+=1
        return maxArea