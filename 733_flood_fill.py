class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n, orig = len(image), len(image[0]), image[sr][sc]

        def dfs(sr, sc):
            if not (0 <= sr < m and 0 <= sc < n) or image[sr][sc] != orig: 
                return
            image[sr][sc] = color
            for (x, y) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(sr + x, sc + y)
        
        if orig != color:
            dfs(sr, sc)

        return image
