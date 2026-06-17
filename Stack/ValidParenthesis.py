class Solution:
    def isValid(self, s: str) -> bool:
        compare = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for c in s:
            if c == ')'  and stack and compare[c] == stack[-1]:
                stack.pop()
            elif c == ']' and stack and compare[c] == stack[-1]:
                stack.pop()
            elif c == '}' and stack and compare[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return True if not stack else False