class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        prev = None
        i = 1
        for num in nums:
            if prev == None:
                prev = num
                continue
            if num == prev:
                continue
            else:
                prev = num
                nums[i] = num
                i+=1
        return i
                
                
                
