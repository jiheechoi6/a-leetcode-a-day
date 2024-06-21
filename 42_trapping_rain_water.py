class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = [0 for _ in range(len(height))]
        maxr = [0 for _ in range(len(height))]

        m = 0
        for i, h in enumerate(height):
            maxl[i] = m
            m = max(m, h)

        m = 0
        for i in range(len(height) - 1, -1, -1):
            maxr[i] = m
            m = max(m, height[i])

        res = 0
        for i, h in enumerate(height):
                res += max(0, min(maxl[i], maxr[i]) - h)

        return res
        
