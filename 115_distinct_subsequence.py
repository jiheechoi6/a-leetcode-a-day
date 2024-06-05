class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[j][i] += dp[j-1][i]
                if s[j-1] == t[i-1]: dp[j][i] += dp[j-1][i-1]

        return dp[-1][-1]
