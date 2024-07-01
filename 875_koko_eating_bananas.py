class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxpile = max(piles)
        l, r = 1, maxpile

        while l < r:
            mid = (l + r) // 2

            hrs = 0
            for pile in piles:
                hrs += ceil(pile / mid)

            if hrs > h: l = mid + 1
            else: r = mid
        
        return l
        
