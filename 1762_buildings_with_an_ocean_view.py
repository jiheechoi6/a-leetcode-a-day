class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights)-1]

        for idx in range(len(heights)-2, -1, -1):
            if heights[idx] > heights[res[-1]]:
                res.append(idx)
        
        res.reverse()
        return res
