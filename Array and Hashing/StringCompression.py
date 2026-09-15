class Solution:
    def compress(self, chars) -> int:
        if len(chars)==1:
            return 1
        l = 0
        r = 0
        i = 0
        n = len(chars)
        while r < n:
            if chars[r]!=chars[l]:
                if r - l > 1:
                    chars[i]=(chars[l])
                    i+=1
                    if r-l > 9:
                        count = str(r - l)
                        for j in range(len(count)):
                            chars[i] = count[j]
                            i+=1
                    else:
                        chars[i] = (str(r-l))
                        i+=1
                else:
                    chars[i] = (chars[l])
                    i+=1
                l = r
            r+=1
        if l != r:
            chars[i] = (chars[l])
            i+=1
            if r - l > 1:
                count = str(r-l)
                for j in range(len(count)):
                    chars[i] = count[j]
                    i+=1
        return i