class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        l, r = 0, minSize
        charCnts = defaultdict(int)
        substrCnts = defaultdict(int)
        uniqueCnt = 0

        for i in range(minSize):
            if charCnts[s[i]] == 0: uniqueCnt += 1
            charCnts[s[i]] += 1

        res = 0
        while r <= len(s):
            if uniqueCnt <= maxLetters:
                substrCnts[s[l:r]] += 1
                res = max(res, substrCnts[s[l:r]])

            if r >= len(s): break
            charCnts[s[l]] -= 1
            if charCnts[s[l]] == 0: uniqueCnt -= 1
            charCnts[s[r]] += 1
            if charCnts[s[r]] == 1: uniqueCnt += 1
            l += 1
            r += 1

        return res
