class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            while(deque and nums[deque[-1]] < num):
                deque.pop()     # 2
            if(deque and i - deque[0] >= k):
                deque.popleft() # 3
            deque.append(i)
            res.append(nums[deque[0]])

        return res[k-1:]
        
