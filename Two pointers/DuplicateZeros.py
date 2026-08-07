class Solution:
    def duplicateZeros(self, arr) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                j = len(arr)-1
                while j > i:
                    arr[j] = arr[j-1]
                    j-=1
                i+=2
            else:
                i+=1
        return arr
        

        