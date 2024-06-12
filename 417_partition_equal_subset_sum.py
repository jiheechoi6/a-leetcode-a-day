class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0

        for num in nums:
            sum += num
        
        if (sum % 2) == 1:
            return False
        sum //= 2

        dp = [False for i in range(sum+1)]
        dp[0] = True
        for num in nums:
            for i in range(sum, 0, -1):
                if num <= i: dp[i] = dp[i] or dp[i-num]
        
        return dp[-1]
