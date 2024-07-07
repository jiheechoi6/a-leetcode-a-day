class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stk = [-1]
        heights.append(0)

        for i, h in enumerate(heights):
            while len(stk) and heights[stk[-1]] > h:
                res = max(res, heights[stk.pop()] * (i - stk[-1] - 1))
            
            stk.append(i)

        return res
        
