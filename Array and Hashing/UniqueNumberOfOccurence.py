class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        count = {}
        contain = set()
        for i in arr:
            count[i] = 1 + count.get(i,0)
        for i in count:
            if count[i] in contain:
                return False
            contain.add(count[i])
        return True