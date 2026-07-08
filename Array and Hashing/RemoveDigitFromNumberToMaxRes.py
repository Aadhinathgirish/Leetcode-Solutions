class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        output = 0
        for i in range(len(number)):
            ans = ''
            res = 0
            if number[i] == digit:
                ans = number[0:i]+number[i+1:len(number)]
                res = int(ans)
            output = max(res,output)
        return str(output)
            
            
        
#just concatente strings
            
        