class MaxStack:

    def __init__(self):
        self.heap = []
        self.stk = []
        self.softdel = set()
        self.next_id = 0

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, self.next_id))
        self.stk.append((x, self.next_id))
        self.next_id -= 1

    def _cleanStack(self) -> None:
        while self.stk[-1][1] in self.softdel: 
            self.softdel.remove(self.stk[-1][1])
            self.stk.pop()

    def pop(self) -> int:
        self._cleanStack()
        popped = self.stk.pop()
        self.softdel.add(popped[1])
        return popped[0]

    def top(self) -> int:
        self._cleanStack()
        return self.stk[-1][0]

    def _cleanHeap(self) -> None:
        while self.heap[0][1] in self.softdel: 
            self.softdel.remove(self.heap[0][1])
            heapq.heappop(self.heap)

    def peekMax(self) -> int:
        self._cleanHeap()
        return -self.heap[0][0]

    def popMax(self) -> int:
        self._cleanHeap()
        popped = heapq.heappop(self.heap)
        self.softdel.add(popped[1])
        return -popped[0]

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
