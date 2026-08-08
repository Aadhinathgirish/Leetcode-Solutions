class Solution:
    def reverseWords(self, s: str) -> str:
        r = 0
        res = []
        while r < len(s):
            while s[r] == ' ':
                r+=1
            l = r
            while l < len(s) and s[l] != ' ':
                l+=1
            res.append(s[r:l][::-1])
            r = l
        return ' '.join(res)
        