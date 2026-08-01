class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        count = {0:1}
        ans = 0
        res = 0
        for i in nums:
            ans += i
            if (ans%k) in count:
                res += count[ans%k]
            count[ans%k] = 1 + count.get((ans%k),0)
        return res
