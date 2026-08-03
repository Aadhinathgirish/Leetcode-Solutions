class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        candy = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= candy:
                result.append(True)
            else:
                result.append(False)
        return result