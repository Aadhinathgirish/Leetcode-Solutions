class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        contain = set()
        l,r=0,0
        while r<len(s):
            if s[r] in contain:
                contain.remove(s[l])
                l=l+1
            else:
                contain.add(s[r])
                length = max(length,r-l+1)
                r+=1
                
        return length
        