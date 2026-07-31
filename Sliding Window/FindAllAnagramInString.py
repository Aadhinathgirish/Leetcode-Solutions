class Solution:
    def findAnagrams(self, s: str, p: str):
        countp = {}
        counts = {}
        for i in p:
            countp[i] = 1 + countp.get(i,0)
        k = len(p)
        l = 0
        r = 0
        ans = []
        while r < len(s):
            counts[s[r]] = 1 + counts.get(s[r],0)
            if r - l + 1 == k:
                if counts == countp:
                    ans.append(l)
                counts[s[l]] -=1
                if counts[s[l]] == 0:
                    counts.pop(s[l])
                l+=1
            r+=1
        return ans
                