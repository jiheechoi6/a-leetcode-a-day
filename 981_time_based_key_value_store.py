class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        vals = self.d.get(key, [])

        left, right = 0, len(vals) - 1
        while left <= right:
            mid = (left + right) // 2

            if vals[mid][0] <= timestamp:
                left = mid + 1
                res = vals[mid][1]
            else:
                right = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
