class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        cnt = 1

        for num in nums[1:]:
            if cnt == 0 and num != candidate:
                candidate = num
                cnt = 1
                continue

            if num == candidate:
                cnt += 1
            else:
                cnt -= 1

        return candidate
            
