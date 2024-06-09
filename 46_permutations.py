class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, res, [])
        return res
        
    def backtrack(self, nums, res, path):
        if len(path) == len(nums):
            res.append(path)
            return

        for num in nums:
            self.backtrack(nums, res, path + [num])
