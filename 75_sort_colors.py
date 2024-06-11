class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, len(nums) - 1

        while w <= b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                r, w = r+1, w+1
            elif nums[w] == 1:
                w += 1
            elif nums[w] == 2:
                nums[b], nums[w] = nums[w], nums[b]
                b -= 1
        
        return nums
