class MovingAverage:

    def __init__(self, size: int):
        self.sum = 0
        self.size = size
        self.curSize = 0
        self.que = deque()

    def next(self, val: int) -> float:
        if self.curSize < self.size:
            self.curSize += 1
        else:
            self.sum -= self.que.popleft()
        self.que.append(val)
        self.sum += val

        return self.sum/self.curSize


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
