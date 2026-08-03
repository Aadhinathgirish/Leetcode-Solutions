class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a,b):
            while b!=0:
                a,b = b , a%b
            return a
        ans = ''
        if str1 + str2 != str2 + str1:
            return ''
        num = gcd(len(str1),len(str2))
        if len(str1) < len(str2):
            ans = str1[0:num]
        else:
            ans = str2[0:num]
        return ans