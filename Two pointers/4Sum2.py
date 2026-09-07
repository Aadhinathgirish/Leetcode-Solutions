class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        hashmap = {}
        count = 0
        for i in nums1:
            for j in nums2:
                hashmap[i+j] = 1 + hashmap.get(i+j,0)
        for i in nums3:
            for j in nums4:
                if -(i+j) in hashmap:
                    count+=hashmap[-(i+j)]
        return count
