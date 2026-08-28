class Solution:
    def maxSatisfied(self, customers, grumpy, minutes: int) -> int:
        l = 0
        r = 0
        count = 0
        maxcount= 0
        window = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                count += customers[i]
        while r < len(grumpy):
            if r-l+1 > minutes:
                if grumpy[l] == 1:
                    window -= customers[l]
                l+=1
            else:
                if grumpy[r] == 1:
                    window += customers[r]
                r+=1
            maxcount = max(maxcount,window)
        return count+maxcount

                
