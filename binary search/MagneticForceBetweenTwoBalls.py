class Solution:
    def maxDistance(self, position, m: int) -> int:
        def check(position,m,force):
            last = position[0]
            count =1
            for i in position:
                if abs(i-last) >= force:
                    count+=1
                    last = i
            return count >= m
        position.sort()
        l = 1
        r = max(position)-min(position)
        ans = 0
        while l <= r:
            mid = l + ((r-l))//2
            if check(position,m,mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans