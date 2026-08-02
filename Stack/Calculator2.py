class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operator = '+'
        number = 0
        s = ''.join(s)
        for i,c in enumerate(s):
            if c.isdigit():
                number = (number * 10) + int(c)
            if c == '+' or c == '-' or c =='*' or c =='/' or i == len(s)-1:
                if operator == '+':
                    stack.append(number)
                elif operator == '-':
                    stack.append(-number)
                elif operator == '*':
                    newnum = stack.pop()
                    stack.append(number * newnum)
                else:
                    newnum = stack.pop()
                    stack.append(int(newnum/number))
                if c == '+':
                    operator = '+'
                    number = 0
                elif c == '*':
                    operator = '*'
                    number = 0
                elif c == '-':
                    operator = '-'
                    number = 0
                else:
                    operator = '/'
                    number = 0
        return sum(stack)
            

        