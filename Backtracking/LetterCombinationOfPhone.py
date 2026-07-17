class Solution:
    def letterCombinations(self, digits: str):
        ans = {2:['a','b','c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z']
        }
        index = 0
        res = []
        def backtracking(current,index):
            if len(current) == len(digits):
                output = ''.join(current.copy())
                res.append(output)
                return
            digit = int(digits[index])
            for i in ans[digit]:
                current.append(i)
                backtracking(current,index+1)
                current.pop()
                
        backtracking([],index)
        return res