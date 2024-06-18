class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        fset = set(forbidden)
        right = len(word) - 1
        res = 0

        for left in range(len(word) - 1, -1, -1):
            for j in range(left, min(left + 10, right + 1)):
                if word[left: j+1] in fset:
                    right = j - 1
                    break

            res = max(res, right - left + 1)
        
        return res
        
