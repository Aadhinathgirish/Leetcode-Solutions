class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        n = len(cardPoints)
        window = n - k
        if window == 0:
            return sum(cardPoints)
        l = 0
        r = 0
        ans=0
        minval = sum(cardPoints)
        while r < n:
            ans+= cardPoints[r]
            if r-l+1 > window:
                ans-=cardPoints[l]
                l+=1
            if r-l+1 == window:
                minval = min(ans,minval)
            r+=1
        return sum(cardPoints) - minval