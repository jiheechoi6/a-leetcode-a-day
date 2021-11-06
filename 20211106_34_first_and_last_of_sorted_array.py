class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums): return [-1, -1]    
    
        def findLeft(l, r):
            if l==r: return l
            mid = int(l+(r-l)/2)
            if nums[mid]>= target: return findLeft(l, mid)
            else: return findLeft(mid+1, r)
                
        def findRight(l, r):
            if l==r: return r
            mid = int(l+(r-l)-(r-l)//2)
            if nums[mid] <= target: return findRight(mid, r)
            else: return findRight(l, mid-1)
            
        l, r =  findLeft(0, len(nums)-1), findRight(0, len(nums)-1)   
        if nums[l] != target or nums[r] != target: return[-1, -1]
        else: return [l, r]
