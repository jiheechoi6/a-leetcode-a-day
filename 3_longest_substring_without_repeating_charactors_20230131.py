class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        history = {}
        start_idx = -1
        max_len = 0

        for i in range(len(s)):
            if s[i] in history and history[s[i]]>start_idx:
                max_len = max(max_len, i-start_idx-1)
                start_idx = history[s[i]]
            history[s[i]] = i
        return max(max_len, len(s)-start_idx-1)
