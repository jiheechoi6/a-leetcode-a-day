class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        history = {s[0]: 0}
        cur_len = 1
        max_len = 1

        for i in range(1, len(s)):
            if s[i] in history and (i - cur_len) <= history[s[i]]:
                cur_len = i - history[s[i]]
            else:
                cur_len += 1
            
            max_len = max(max_len, cur_len)
            history[s[i]] = i

        return max_len
