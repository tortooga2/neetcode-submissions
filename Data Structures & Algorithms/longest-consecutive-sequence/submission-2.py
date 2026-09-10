class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = defaultdict(int)
        longest = 0
        for i in nums:
            if not h[i]:   
                length = h[i - 1] + h[i + 1] + 1
                h[i] = length
                h[ i - h[i - 1] ] = length
                h[ i + h[i + 1] ]   = length
                longest = max(longest, h[i])
        return longest


        