class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        counts1,counts2 = {},{}
        for s in s1:
            counts1[s] = 1 + counts1.get(s,0)
        for r in range(len(s1)):
            counts2[s2[r]] = 1 + counts2.get(s2[r],0)
        if counts1 == counts2:
            return True
        l = 0
        for r in range(len(s1),len(s2)):
            counts2[s2[l]] -= 1
            if counts2[s2[l]] == 0:
                counts2.pop(s2[l])
            l+=1
            counts2[s2[r]] = 1 + counts2.get(s2[r],0)
            if counts2 == counts1:
                return True
            r+=1
        return False

