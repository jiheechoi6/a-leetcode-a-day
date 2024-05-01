class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numMap:
                return [numMap[diff], i]
            numMap[nums[i]] = i

        return []
