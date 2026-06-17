class Solution:
    def calPoints(self, operations) -> int:
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-2]+stack[-1])
            elif op == 'D':
                stack.append(2*stack[-1])
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        output = 0
        for i in stack:
            output+=i
        return output
        