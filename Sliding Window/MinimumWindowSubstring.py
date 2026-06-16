class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS,countT = {},{}
        if len(t)>len(s):
            return ''
        output=float('inf')
        res=[-1,-1]
        for i in t:
            countT[i] = 1 + countT.get(i,0)
        need = len(countT)
        l=0
        have=0
        for r in range(len(s)):
            if s[r] in countT:
                countS[s[r]] = 1 + countS.get(s[r],0)
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have+=1
            while need == have:
                if r-l+1 < output:
                    res = [l,r]
                    output = r-l+1
                if s[l] in countT:
                    countS[s[l]]-=1
                if s[l] in countT and countS[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        
        return s[l:r+1] if output!=float('inf') else ''    



        