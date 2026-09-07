class StockSpanner:

    def __init__(self):
        self.st:List[int] = []

    def next(self, price: int) -> int:
        self.st.append(price)
        counter:int = 0
        cp = self.st.copy()

        while cp and cp[-1] <= price:
            counter += 1
            cp.pop()

        return counter


         
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)