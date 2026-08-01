class Solution:
    def buildArray(self, target,n: int):
            output = []
            def push(val,output):
                output.append('Push')
                return output
            def pushpop(val,output):
                output.append('Push')
                output.append('Pop')
                return output 
            j = 0
            for i in range(1,n+1):
                if j < len(target):
                    if i == target[j]:
                        push(i,output)
                        j+=1
                    else:
                        pushpop(i,output)
                else:
                    return output
            return output