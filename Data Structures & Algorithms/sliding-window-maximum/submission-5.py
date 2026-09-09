class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        
        for val, index in enumerate(nums):
            while q and nums[q[-1]] < index:
                q.pop()
            q.append(val)
            
            if q[0] <= val - k:
                q.popleft()
                
            if val >= k - 1:
                res.append(nums[q[0]])
                
        return res
        