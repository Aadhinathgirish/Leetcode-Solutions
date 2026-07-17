class Solution:
    def permute(self, nums):
        check = {num:False for num in nums}
        res = []
        def backtracking(current,check):
            if len(current) == len(nums):
                res.append(current.copy())
                return
            for i in nums:
                if check[i]:
                    continue
                current.append(i)
                check[i] = True
                backtracking(current,check)
                current.pop()
                check[i] = False
        backtracking([],check)
        return res