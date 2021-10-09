class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        capital_q = []
        for i in range(len(profits)):
            capital_q.append((capital[i], profits[i]))
        
        heapify(capital_q)
        avail_p = []  # max heap
        
        for i in range(k):
            while len(capital_q) != 0 and capital_q[0][0] <= w:
                heappush(avail_p, -heappop(capital_q)[1])
            
            if len(avail_p) == 0:
                return w
            
            w -= heappop(avail_p)
            
        return w
        
