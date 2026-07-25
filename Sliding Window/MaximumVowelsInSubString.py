class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxVowel = 0
        count = 0
        vowels = ['a','e','i','o','u']
        while r < len(s):
            if r - l + 1 > k:
                if s[l] in vowels:
                    count -=1
                l+=1
            if s[r] in vowels:
                count+=1
            maxVowel = max(maxVowel,count)
            r+=1
        return maxVowel
        