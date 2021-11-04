class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:    return 0
        
        idx=1
        prev = nums[0]
        
        for num in nums[1:]:
            if prev != num:
                nums[idx] = num
                idx += 1
            prev = num
        
        return idx
                
