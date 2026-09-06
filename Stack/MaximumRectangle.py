class Solution:
    def maximalRectangle(self, matrix) -> int:
        def histogram(arr):
            stack = []
            maxarea = 0
            for i in range(len(arr)):
                while stack and arr[stack[-1]] > arr[i]:
                    area = 0
                    heights = stack.pop()
                    if stack:
                        area = arr[heights] * (i-stack[-1]-1)
                    else:
                        area = arr[heights] * i
                    maxarea = max(area,maxarea)
                stack.append(i)
            while stack:
                area = 0
                heights = stack.pop()
                if stack:
                    area = arr[heights] * (len(arr)-stack[-1]-1)
                else:
                    area = arr[heights] * len(arr)
                maxarea = max(area,maxarea)
            return maxarea

        maxArea = 0
        height = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    height[j] +=1
                else:
                    height[j] = 0
            ans = histogram(height)
            maxArea = max(maxArea,ans)
        return maxArea
