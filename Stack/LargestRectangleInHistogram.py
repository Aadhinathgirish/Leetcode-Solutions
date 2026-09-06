class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = []
        maxarea = 0
        for i in range(len(heights)):
                    while stack and heights[stack[-1]]>heights[i]:
                        area = 0
                        height = stack.pop()
                        if stack:
                            area = heights[height] *(i-stack[-1]-1)
                        else:
                            area = heights[height] * (i-0)
                        maxarea = max(maxarea,area)
                    stack.append(i)
        while stack:
            area = 0
            height = stack.pop()
            if stack:
                area = heights[height] * (len(heights)-stack[-1]-1)
            else:
                area = heights[height] * len(heights)
            maxarea = max(area,maxarea)
        return maxarea