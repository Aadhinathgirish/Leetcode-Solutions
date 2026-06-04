def validpalindrome(s):
    res=''
    whitespace =['/','?',' ','!']
    for char in s:
        if char not in whitespace:
            res+=char
    l,r = 0,len(res)-1
    while l<r:
        if res[l] != res[r]:
            return False
        l+=1
        r-=1
    return True

print(validpalindrome('Was it a car or a cat I saw?'))