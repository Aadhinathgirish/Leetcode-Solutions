from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        for i in range(len(senate)):
            if senate[i] == 'D':
                dire.append(i)
            else:
                radiant.append(i)
        n = len(senate)
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant.popleft()+n)
                dire.popleft()
            else:
                dire.append(dire.popleft()+n)
                radiant.popleft()
        return "Radiant" if radiant else "Dire"
