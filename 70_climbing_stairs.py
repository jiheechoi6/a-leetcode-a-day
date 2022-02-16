class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2  # a-> # of steps for previous stair, b-> # of steps for current stair
        if n == 1: return a
        if n == 2: return b
        for _ in range(3, n+1):
            a, b = b, a+b
            
        return b
