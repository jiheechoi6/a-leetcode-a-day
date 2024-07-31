class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtrack(candidates, res, [], 0, target)
        return res

    def backtrack(self, candidates, res, path, start, target):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return

        for i in range(start, len(candidates)):
            self.backtrack(candidates, res, path + [candidates[i]], i, target - candidates[i])
