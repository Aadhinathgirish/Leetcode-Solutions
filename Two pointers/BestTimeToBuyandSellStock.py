class Solution:
    def maxProfit(self, prices) -> int:
        maxprofit = 0
        minval = prices[0]
        for i in prices:
            maxprofit = max(maxprofit,i-minval)
            if i < minval:
                minval = i
        return maxprofit
                

                