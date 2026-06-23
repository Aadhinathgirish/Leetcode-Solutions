class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        sp = 1
        while self.stack and self.stack[-1][0] <= price:
            pri,span = self.stack.pop()
            sp+=span
        self.stack.append([price,sp])
        return sp
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)