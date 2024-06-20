class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnts = Counter(nums)
        res = 0

        for cnt in cnts.values():
            if cnt == 1: return -1
            res += (cnt//3)

            if cnt % 3: res += 1
        
        return res
        
