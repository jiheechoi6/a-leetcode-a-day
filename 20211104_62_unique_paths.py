import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        bigger = max(m, n)
        smaller = min(m, n)
        denom = 1
        for i in range(bigger, m+n-1):
            denom = denom*i
        return int(denom/math.factorial(smaller-1))
