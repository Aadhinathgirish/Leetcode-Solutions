class Solution:

    def __init__(self,s):
        self.s = s
    def reverseString(self) -> None:
                l,r = 0,len(self.s)-1
                while l<r:
                    self.s[l],self.s[r]=self.s[r],self.s[l]
                    l+=1
                    r-=1
                return self.s
sol = Solution(['h','e','l','l','o'])
print(sol.reverseString())
sol2 = Solution(['h','e','n','s','r','d'])
print(sol2.reverseString())

       
        