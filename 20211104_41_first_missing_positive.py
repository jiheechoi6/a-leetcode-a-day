class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        cnts = [0]*(l+1)
        
        for num in nums:
            if num >0 and num <= l:
                cnts[num] += 1
        
        for i, cnt in enumerate(cnts[1:]):
            if cnt == 0:
                return i+1
        
        return l+1
