class Solution:
    def findLongestWord(self, s: str, dictionary) -> str:
        ans = ''
        for i in dictionary:
            l = 0
            r = 0
            while l < len(s) and r < len(i):
                if s[l] == i[r]:
                    l+=1
                    r+=1
                else:
                    l+=1
            if r == len(i):
                if len(ans)<len(i):
                    ans = i
                elif len(ans) == len(i):
                    if i < ans:
                        ans = i
        return ans


                          