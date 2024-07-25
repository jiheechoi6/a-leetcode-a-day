class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        idxmap = {}

        for i, ch in enumerate(s):
            # ch exists on the left
            if ch in idxmap:
                l = max(idxmap[ch] + 1, l)
            idxmap[ch] = i

            max_len = max(max_len, i - l + 1)

        return max_len
