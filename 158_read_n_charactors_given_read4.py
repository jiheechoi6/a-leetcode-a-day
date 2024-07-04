# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.bufload = deque()

    def read(self, buf: List[str], n: int) -> int:
        readcnt = 0
        buf4 = ['']*4

        while readcnt < n:
            if len(self.bufload) == 0:
                for i in range(read4(buf4)):
                    self.bufload.append(buf4[i])
                if not self.bufload:
                    break
            buf[readcnt] = self.bufload.popleft()
            readcnt += 1

        return readcnt
