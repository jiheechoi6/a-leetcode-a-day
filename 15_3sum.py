class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums)-1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]

                if sum3 > 0: r -= 1
                elif sum3 < 0: l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1

        return res

