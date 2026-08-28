class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        r = 0
        counts = 0
        count = {}
        while r < len(s):
            count[s[r]] = 1 + count.get(s[r],0)
            while len(count) == 3:
                counts+= len(s) - r
                count[s[l]] -=1
                if count[s[l]] == 0:
                    count.pop(s[l])
                l+=1
            r+=1
        return counts

           
            
            