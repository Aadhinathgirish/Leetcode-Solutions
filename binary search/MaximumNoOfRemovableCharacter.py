class Solution:
    def maximumRemovals(self, s: str, p: str, removable) -> int:
        def remove(s,p,num):
            l = 0
            removed = set(removable[:num])
            for i in range(len(s)):
                if i in removed:
                    continue
                if l == len(p):
                    return True
                else:
                    if s[i] == p[l]:
                        l+=1
            return True if l >= len(p) else False  
            

        l = 1
        r = len(removable)
        ans = 0
        while l <= r:
            mid = l + (r-l)//2
            if remove(s,p,mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans
            
