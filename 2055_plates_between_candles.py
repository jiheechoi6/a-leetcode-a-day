class Solution:
    def bisect_left(self, lst, item):
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if lst[mid] < item: lo = mid + 1
            else: hi = mid
        return lo
    
    def bisect_right(self, lst, item):
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi)// 2
            if lst[mid] > item: hi = mid
            else: lo = mid + 1
        return lo

    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ci = []
        for i, ch in enumerate(s):
            if ch == '|': ci.append(i)
        res = []
        for l, r in queries:
            lc = self.bisect_left(ci, l)
            rc = self.bisect_right(ci, r) - 1

            res.append((ci[rc] - ci[lc]) - (rc - lc) if lc < rc else 0)
        
        return res
