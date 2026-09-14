class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 0:
            return float("infinity")
        
        #find middle
        mid = n // 2
        num1 = self.findMin(nums[:mid])
        num2 = self.findMin(nums[mid:])

        return min(num1, num2)


        
        