class Solution:
    def simplifyPath(self, path: str) -> str:
        cur =''
        r=0
        stack=[]
        for r in path + '/':
            if r!='/':
                cur+=r
            else:
                if cur == '..':
                    if stack:
                        stack.pop()
                    cur=''
                elif cur:
                    if cur != '.':
                        stack.append(cur)
                    cur=''
        output = '/'.join(stack)
        return f'/{output}'