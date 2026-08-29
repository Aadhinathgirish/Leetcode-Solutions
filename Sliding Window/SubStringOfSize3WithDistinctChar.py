class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        r = 0
        count = {}
        ans = 0
        while r < len(s):
            count[s[r]] = 1 + count.get(s[r],0)
            if r - l + 1 > 3:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l])
                l+=1
            if r-l+1 == 3:
                if len(count) == 3:
                    ans+=1
            r+=1
        return ans