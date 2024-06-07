class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval
            elif newInterval[0] < interval[1] or newInterval[1] > interval[0]:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]

        result.append(newInterval)

        return result
