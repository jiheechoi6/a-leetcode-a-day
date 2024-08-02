class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        i1, i2 = 0, 0
        self.lst = []
        while i1 < len(v1) or i2 < len(v2):
            if i1 < len(v1):
                self.lst.append(v1[i1])
                i1 += 1
            if i2 < len(v2):
                self.lst.append(v2[i2])
                i2 += 1

        self.idx = 0

    def next(self) -> int:
        val = self.lst[self.idx]
        self.idx += 1
        return val

    def hasNext(self) -> bool:
        return self.idx < len(self.lst)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
