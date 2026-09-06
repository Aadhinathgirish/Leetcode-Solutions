class Solution:
    def sumSubarrayMins(self, arr) -> int:
        left = [0] * len(arr)
        right = [0] * len(arr)
        stack1 = []
        stack2 = []
        for i in range(len(arr)):
            while stack1 and arr[stack1[-1]] >= arr[i]:
                ans = stack1.pop()
                if stack1:
                    left[ans] = stack1[-1]
                else:
                    left[ans] = -1
            stack1.append(i)
        while stack1:
            ans = stack1.pop()
            if stack1:
                left[ans] = stack1[-1]
            else:
                left[ans] = -1
        for i in range(len(arr)-1,-1,-1):
            while stack2 and arr[stack2[-1]] > arr[i]:
                ans = stack2.pop()
                if stack2:
                    right[ans] = stack2[-1]
                else:
                    right[ans] = len(arr)
            stack2.append(i)
        while stack2:
            ans = stack2.pop()
            if stack2:
                right[ans] = stack2[-1]
            else:
                right[ans] = len(arr)
        output = 0
        for i in range(len(arr)):
            output += arr[i] *((i-left[i])*(right[i]-i))
        return output % (10**9 + 7)
