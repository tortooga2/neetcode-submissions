class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = sorted(list(set(nums)))
        start = 0
        end = 0
        longest = 0
        while start < len(s):
            end = start
            while end + 1 < len(s) and s[end + 1] - s[end] == 1:
                end += 1
            longest = max(longest, end - start + 1)
            start = end + 1
        return longest
