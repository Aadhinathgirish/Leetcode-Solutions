class Solution:
    def validPalindrome(self, s: str) -> bool:
        def Palindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        l = 0
        r = len(s) - 1
        k = 1
        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return Palindrome(l+1,r) or Palindrome(l,r-1)
        return True
                