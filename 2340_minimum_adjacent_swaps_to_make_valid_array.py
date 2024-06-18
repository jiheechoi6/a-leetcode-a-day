class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        mini = 0
        maxi = len(nums) - 1

        for i, num in enumerate(nums):
            if nums[mini] > num:
                mini = i
            if nums[maxi] <= num:
                maxi = i
        
        res = (len(nums)-1 - maxi) + mini

        return res if mini <= maxi else res - 1
