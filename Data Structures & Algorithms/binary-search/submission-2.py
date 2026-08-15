class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        i = (end-start)//2
        while (end - start) >= 1:
            if nums[i] == target:
                return i
            if nums[i] > target:
                end = i
            if nums[i] < target:
                start = i + 1
            
            if start >= end:
                break
            i = start + (end-start)//2
        
        return -1
