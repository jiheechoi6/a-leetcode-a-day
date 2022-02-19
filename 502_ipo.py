class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pro_cap = sorted(zip(profits, capital), key=lambda x:x[1])
        heap = []
        add_idx = 0
        
        for _ in range(k):
            while add_idx<len(profits) and w>=pro_cap[add_idx][1]:
                heapq.heappush(heap, -pro_cap[add_idx][0]).  # max heap
                add_idx += 1
            
            if not heap: return w
            w -= heapq.heappop(heap)

        return w
