class Solution:
    def __init__(self):
        self.letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        self.dfs(digits, 0, "", res)

        return res
    
    def dfs(self, digits, idx, cur, res):
        if idx == len(digits): 
            res.append(cur)
            return

        for l in self.letters[int(digits[idx])]:
            self.dfs(digits, idx+1, cur+l, res)
        
