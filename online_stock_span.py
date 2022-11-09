class StockSpanner:

    def __init__(self):
        self.result = []
        

    def next(self, price: int) -> int:
        days = 1
        while self.result and self.result[-1][0] <= price:
            days += self.result.pop()[1]
        self.result.append([price, days])
        return days
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
