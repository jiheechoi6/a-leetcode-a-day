class Solution:

    def __init__(self, w: List[int]):
        self.cdf = [0]

        for i, n in enumerate(w):
            self.cdf.append(self.cdf[i]+n)

    def pickIndex(self) -> int:
        ran = random.randint(1, self.cdf[-1])
        idx = bisect.bisect_left(self.cdf, ran)

        return idx - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
