class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        ans = [intervals[0]]
        for time in intervals:
            if time[0] <= ans[-1][1]:
                ans[-1][1] = max(time[1], ans[-1][1])
            else:
                ans.append(time)
                
        return ans
