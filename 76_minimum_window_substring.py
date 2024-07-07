class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missingCnt, missingMap = len(t), defaultdict(int)

        for ch in t:
            missingMap[ch] += 1

        start, end = 0, 0
        resStartIdx = 0
        minLen = math.inf

        while end < len(s):
            if s[end] not in missingMap:
                end += 1
                continue

            if missingMap[s[end]] > 0: missingCnt -= 1            
            missingMap[s[end]] -= 1
            end += 1

            while missingCnt == 0:
                if (end - start) < minLen:
                    minLen = end - start
                    resStartIdx = start

                if s[start] in missingMap:
                    missingMap[s[start]] += 1
                    if missingMap[s[start]] > 0: missingCnt += 1

                start += 1
                
        return "" if minLen == math.inf else s[resStartIdx: resStartIdx + minLen]
        
