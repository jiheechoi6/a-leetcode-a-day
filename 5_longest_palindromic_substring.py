class Solution:
    def _palindrome(self, cl, cr, s) -> str:
        while cl >= 0 and cr < len(s) and s[cl] == s[cr]:
            cl -= 1
            cr += 1

        return s[cl + 1: cr] 

    def longestPalindrome(self, s: str) -> str:
        res = s[0]

        for i in range(0, len(s) - 1):
            odd = self._palindrome(i, i, s)
            even = self._palindrome(i, i+1, s)

            res = odd if len(odd) > len(res) else res
            res = even if len(even) > len(res) else res

        return res
