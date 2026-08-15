class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        i = (end-start)//2
        while start < end:
            i = start + ((end - start) // 2)
            if nums[i] > target:
                end = i
            if nums[i] < target:
                start = i + 1
            if nums[i] == target:
                return i
        return -1
