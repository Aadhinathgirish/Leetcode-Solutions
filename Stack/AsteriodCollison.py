class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for a in asteroids:
            while stack and a<0 and  stack[-1]>0:
                    res = a + stack[-1]
                    if res < 0:
                        stack.pop()
                    elif res == 0:
                        stack.pop()
                        a=0
                        break
                    else:
                        a=0
            if a:
                stack.append(a)
        return stack

            