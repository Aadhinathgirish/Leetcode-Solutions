class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countr = {}
        countm = {}
        for i in ransomNote:
            countr[i] = 1 + countr.get(i,0)
        for i in magazine:
            countm[i] = 1 + countm.get(i,0)
        for i in countr:
            if i in countm:
                if countr[i] > countm[i]:
                    return False
            else:
                return False
        return True