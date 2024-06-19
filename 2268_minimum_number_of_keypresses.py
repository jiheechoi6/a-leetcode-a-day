class Solution:
    def minimumKeypresses(self, s: str) -> int:
        sortedCnt = sorted(Counter(list(s)).items(), key=lambda x: -x[1])

        res = 0
        # first letters
        counts = sortedCnt[:9] if len(sortedCnt) > 9 else sortedCnt[:]
        res += sum(cnt for _, cnt in counts)

        # second letters
        counts = sortedCnt[9:18] if len(sortedCnt) > 18 else sortedCnt[9:]
        res += (sum(cnt for _, cnt in counts)*2)

        # third letters
        res += (sum(cnt for _, cnt in sortedCnt[18:])*3)

        return res
