class Listnode:
    def __init__(self,key):
        self.key = key
        self.next = None

class Hashset:
    def __init__(self):
        self.set = [Listnode[0] for i in range(10**4)]

    def addvalue(self,key):
        cur = self.set[key%len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = Listnode[key]
    
    def removevalue(self,key):
        cur = self.set[key%len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
    
    def findelemnet(self,key):
        cur = self.set[key%len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False