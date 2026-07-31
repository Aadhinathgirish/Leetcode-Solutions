class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        maxlen = 0
        while r < len(answerKey):
            count[answerKey[r]] =  1 + count.get(answerKey[r],0)
            while (r - l + 1 - max(count.values())) > k:
                count[answerKey[l]] -=1
                if count[answerKey[l]] == 0:
                    count.pop(answerKey[l])
                l+=1
            maxlen = max(maxlen,r-l+1)
            r+=1
        return maxlen
