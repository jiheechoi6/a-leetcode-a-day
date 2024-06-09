class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, hi = 0, len(nums) - 1

        while low < hi:
            mid = (low + hi)//2
            if nums[mid] > nums[hi]:
                low = mid + 1
            else:
                hi = mid
        
        rot = low
        low, hi = 0, len(nums) - 1

        while low <= hi:
            mid = (low + hi) // 2
            realmid = (mid + rot) % len(nums)

            if nums[realmid] == target: return realmid
            if target > nums[realmid]:
                low = mid + 1
            else:
                hi = mid - 1

        return -1
            
