class MyQueue:

    def __init__(self):
        self.stack = []
        self.revstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.revstack:
            while self.stack:
                self.revstack.append(self.stack.pop())
        return self.revstack.pop() 


    def peek(self) -> int:
        if not self.revstack:
            while self.stack:
                self.revstack.append(self.stack.pop())
        return self.revstack[-1]

    def empty(self) -> bool:
        return True if not self.stack and not self.revstack else False 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()