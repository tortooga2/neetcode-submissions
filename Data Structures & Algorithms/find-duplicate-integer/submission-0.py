class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = {}
        for i in nums:
            count = m.get(i, 0) + 1
            if count > 1:
                return i
            m[i] = count
        return -1
        