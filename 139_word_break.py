class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        ok = [True]
        max_len = max(map(len, words+['']))
        words = set(words)
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(max(0, i-max_len),i)),
        return ok[-1]
        
        
