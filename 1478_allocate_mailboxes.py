class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses = sorted(houses)
        dis = [[0]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dis[i][j] = houses[j] - houses[i]
                if i < j: dis[i][j] += dis[i+1][j-1]
        
        @lru_cache(None)
        def dp(k, i):
            if k == 0 and i == n: return 0
            if k == 0 or i == n: return math.inf

            ans = math.inf
            for j in range(i, n):
                ans = min(ans, dis[i][j] + dp(k -1, j + 1))
            
            return ans
        
        return dp(k, 0)
        
