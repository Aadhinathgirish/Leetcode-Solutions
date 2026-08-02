class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = []
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                        stack.pop()
                else:
                    remove.append(i)
            
        while stack:
            remove.append(stack.pop())
        remove.sort()
        print(remove)
        ans = ''
        for i,c in enumerate(s):
            if i not in remove:
                ans+=c
        return ans

            
        