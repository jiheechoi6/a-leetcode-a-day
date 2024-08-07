class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        self.backtrack(nums, [], 0, res)
        return res

    def backtrack(self, nums, cur, idx, res):
        for i in range(idx, len(nums)):
            cur.append(nums[i])
            res.append(cur.copy())
            self.backtrack(nums, cur, i + 1, res)
            cur.pop()
        
