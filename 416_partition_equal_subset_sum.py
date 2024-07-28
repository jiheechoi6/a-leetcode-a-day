class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if (total % 2) != 0:
            return False

        target = total//2

        # find subset that sums to target
        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for i in range(target, 0, -1):
                if i >= num: dp[i] = dp[i-num] or dp[i]
        
        return dp[-1]
        
