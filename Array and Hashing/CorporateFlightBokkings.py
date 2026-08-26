class Solution:
    def corpFlightBookings(self, bookings, n: int):
        ans = [0] * (n+2)
        for i in range(len(bookings)):
            ans[bookings[i][0]] += bookings[i][2]
            ans[(bookings[i][1])+1] -= bookings[i][2]
        for i in range(1,len(ans)):
            ans[i] = ans[i-1] + ans[i]
        return ans[1:len(ans)-1]