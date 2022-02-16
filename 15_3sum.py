class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # last_idx = len(nums)-1
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:  # skip duplicate
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                s = nums[l]+nums[r]
                if s < -nums[i]:
                    l+=1
                elif s > -nums[i]:
                    r-=1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return result
