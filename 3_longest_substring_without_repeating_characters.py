class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = 0
        result = 0
        
        for i, c in enumerate(s):
            if c in used and start<=used[c]:
                result = max(result, i-start)
                start = used[c]+1
            used[c]=i
        
        return max(result, len(s)-start)
