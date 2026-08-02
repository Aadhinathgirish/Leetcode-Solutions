class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        stack = [-1]
        ans = 0
        count = 0
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    count = i - stack[-1]
                else:
                    stack.append(i)
            ans = max(ans,count)
        return ans
