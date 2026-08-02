class Solution:
    def minInsertions(self, s: str) -> int:
      
        need = 0
        insertions = 0

        for c in s:
            if c == '(':
              
                need += 2

                
                if need % 2 == 1:
                    insertions += 1
                    need -= 1

            else: 
                need -= 1

            
                if need == -1:
                    insertions += 1  
                    need = 1          

        return insertions + need
                
            