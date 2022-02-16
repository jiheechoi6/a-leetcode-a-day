class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums): return [-1, -1]
        
        def findLeft():
            l, r = 0, len(nums)-1
            while l<=r:
                mid = (r+l)//2
                if target > nums[mid]: l = mid+1
                else: r = mid-1
            return l
        
        def findRight():
            l, r = 0, len(nums)-1
            while l<=r:
                mid = (r+l)//2
                if target >= nums[mid]: l = mid+1
                else: r = mid-1
            return r
        
        l, r = findLeft(), findRight()
        if l>r: return [-1, -1]
        return [l, r]
    
