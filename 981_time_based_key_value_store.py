class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.storage[key]
        l, r = 0, len(vals)

        res = ''
        while l < r:
            mid = (l + r) // 2

            if vals[mid][1] > timestamp: r = mid
            else:
                l = mid + 1
                res = vals[mid][0]
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
