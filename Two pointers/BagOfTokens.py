class Solution:
    def bagOfTokensScore(self, tokens, power: int) -> int:
        score = 0
        tokens.sort()
        l = 0
        r = len(tokens)-1
        ans = 0
        while l <=r:
            if tokens[l] <= power:
                power-=tokens[l]
                score+=1
                l+=1
            else:
                if score > 0:
                    power+=tokens[r]
                    score-=1
                    r-=1
                else:
                    return 0
            ans = max(ans,score)
        return ans
        
            
