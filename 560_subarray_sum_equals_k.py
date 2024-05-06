class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, psum, sumdic = 0, 0, {0:1}

        for num in nums:
            psum += num
            if (psum - k) in sumdic:
                ans += sumdic[psum-k]
            sumdic[psum] = sumdic.get(psum, 0)+1
        
        return ans
