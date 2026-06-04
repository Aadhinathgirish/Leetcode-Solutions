from collections import defaultdict
def groupanagram(strs):
    res = defaultdict(list)
    for i in range(len(strs)):
        count = [0] * 26
        for s in strs[i]:
            count[ord(s)-ord('a')] += 1
        res[tuple(count)].append(strs[i])
    return list(res.values())
    
print(groupanagram(['pot','top','eat','tin','ate','nit','eat','owl']))

    




