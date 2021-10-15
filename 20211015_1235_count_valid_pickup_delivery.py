class Solution:
    def countOrders(self, n: int) -> int:
        return self.count(n) % (10**9 + 7)
        
    def count(self, n):
        if n == 1:
            return 1
        return sum(range(1, (n-1)*2+2)) *self.count(n-1)
