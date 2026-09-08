class Solution:
    def findBestValue(self, arr, target: int) -> int:
        total1 = float('inf')
        l = 0
        r = max(arr)
        ans = max(arr)
        while l <= r:
            mid = l + ((r-l)//2)
            total = 0
            for i in arr:
                total += min(i,mid)
            if abs(total - target) < abs(total1 - target):
                    total1 = total
                    ans = mid
            elif abs(total - target) == abs(total1 - target) and  mid < ans:
                ans = mid
            if total > target:
                r = mid - 1
            elif total < target:
                l = mid + 1
            else:
                return mid
        return ans
                
