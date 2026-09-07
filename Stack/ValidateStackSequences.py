class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        j = 0
        for i in pushed:
            while stack and j < len(popped)and stack[-1] == popped[j]:
                stack.pop()
                j+=1
            stack.append(i)
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j+=1

        return True if not stack else False