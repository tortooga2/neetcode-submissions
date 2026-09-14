class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] > nums[r]: #if true we know we are in the left portion, so we want to move our left pointer to mid += 1
                l = mid + 1
            else:
                r = mid
        return nums[l]
                

        