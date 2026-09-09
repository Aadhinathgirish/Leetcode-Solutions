class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def side_sum(index,maxSum,n,val):
            left = index
            right = n-1 -index
            if left < mid:
                first = mid - left
                last = mid-1
                leftSum = ((first +last)*left)//2
            else:
                leftSum = (mid*(mid-1))//2 + (left-(mid-1))
            if right < mid:
                first = mid - right
                last = mid-1
                rightSum = ((first +last)*right)//2
            else:
                rightSum = (mid*(mid-1))//2 + (right-(mid-1))
            return leftSum + rightSum + mid <= maxSum
        
        l = 1
        r = maxSum
        ans = 0
        while l <=r:
            mid = l+ ((r-l)//2)
            if side_sum(index,maxSum,n,mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans
            