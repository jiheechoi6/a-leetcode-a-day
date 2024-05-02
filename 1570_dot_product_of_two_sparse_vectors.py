class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {i: num for i, num in enumerate(nums) if num}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        shorter, other = self.nums, vec.nums

        if len(vec.nums) < len(self.nums):
            shorter, other = vec.nums, self.nums

        result = 0
        for i, num in shorter.items():
            if i in other:
                result += (num * other[i])
        
        return result


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
