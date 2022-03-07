class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        dp = [True]
        words = set(words)
        max_len = max(map(len, words))
        
        for i, ch in enumerate(s):
            dp.append(any(s[j:i+1] in words and dp[j] for j in range(max(0, i-max_len), i+1)))
        
        return dp[-1]
