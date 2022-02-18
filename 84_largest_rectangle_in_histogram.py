class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stk = []
        heights.append(0)
        
        for i, h in enumerate(heights):
            while len(stk) and heights[stk[-1]]>h:
                ans = max(ans, heights[stk.pop()]*(i if not stk else i-stk[-1]-1))
            stk.append(i)
        return ans
