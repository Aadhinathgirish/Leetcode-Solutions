class Solution:
    def intersection(self, nums1, nums2):
        ans = set()
        for i in nums1:
            if i in nums2:
                ans.add(i)
        return list(ans)