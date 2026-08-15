class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == None or nums == []:
            return []
        
        nums = sorted(nums)
        output = []
        
        for i, target in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total < -target:
                    left += 1
                elif total > -target:
                    right -= 1
                else:
                    output.append([target, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return output
