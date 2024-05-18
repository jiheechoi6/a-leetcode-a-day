# DP O(n^2)
class Solution:
    def convertArray(self, nums: List[int]) -> int:
        levels = sorted(set(nums))
        def helper(nums):
            dp = defaultdict(int)
            
            for num in nums:
                cur_res = math.inf
                for cur_level in levels:
                    cur_res = min(cur_res, dp[cur_level]+abs(num-cur_level))
                    dp[cur_level] = cur_res
            return dp[levels[-1]]

        return min(helper(nums), helper(nums[::-1]))


# Max Heap O(nlogn)
class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def helper(nums):
            que = []
            res = 0

            for num in nums:
                if que and num < -que[0]:
                    res += abs(num-(-heapq.heappop(que)))
                    heapq.heappush(que, -num)
                heapq.heappush(que, -num)
            
            return res
        
        return min(helper(nums), helper(nums[::-1]))
