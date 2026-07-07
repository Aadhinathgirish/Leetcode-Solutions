class Solution:
    def sortVowels(self, s: str) -> str:
        res = []
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        for c in s:
            if c in vowels:
                res.append(c)
        res.sort()
        s = list(s)
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = res[j]
                j+=1
        return ''.join(s)






        