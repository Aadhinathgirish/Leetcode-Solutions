class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        def bloom(bloomDay,m,k,days):
            consecutive = 0
            count = 0
            for i in bloomDay:
                if i <= days:
                    consecutive+=1
                if i > days:
                    consecutive = 0
                if consecutive == k:
                    count+=1
                    consecutive = 0 
                
            return count >= m      
        if m * k > len(bloomDay):
            return -1
        l = min(bloomDay)
        r = max(bloomDay)
        while l < r:
            mid = l + ((r-l)//2)
            if bloom(bloomDay,m,k,mid):
                r = mid
            else:
                l=mid+1
        return l
