class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        change = [0]*1001
        for i in range(len(trips)):
            change[trips[i][1]] += trips[i][0]
            change[trips[i][2]] -= trips[i][0]
        current = 0
        for i in change:
            current+=i
            if current > capacity:
                return False
        return True