class Solution:
    def totalFruit(self, fruits) -> int:
        count = {}
        l = 0
        r = 0
        maxlen = 0
        while r < len(fruits):
            count[fruits[r]] = 1 + count.get(fruits[r],0)
            while len(count) > 2:
                count[fruits[l]] -=1
                if count[fruits[l]] == 0:
                    count.pop(fruits[l])
                l+=1
            maxlen = max(maxlen,r - l + 1)
            r+=1
        return maxlen
