class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)

        for i in range(1, len(nums)):
            if (i-1) >=0 and nums[i-1] == nums[i]:
                dp[i] = dp[i-2] if (i-2) >= 0 else True
            if (i-2) >=0 and nums[i-2] == nums[i-1] == nums[i]:
                dp[i] |= (dp[i-3] if (i-3) >= 0 else True)
            if (i-2) >=0 and nums[i-2] == (nums[i]-2) and nums[i-1] == (nums[i]-1):
                dp[i] |= (dp[i-3] if (i-3) >= 0 else True)

        return dp[-1]
