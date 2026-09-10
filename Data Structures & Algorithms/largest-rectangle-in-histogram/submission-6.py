class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [] #(height, index) we pop if the ith h < i-1th (gotten from end of stack), we place h, i-ths index) an pop i-1. 
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while s and h < s[-1][0]:
                old_h, old_i = s.pop()
                max_area = max(max_area, old_h * (i - old_i))
                start = old_i
            s.append((h, start))
        
        n = len(heights)
        while s:
            h, i = s.pop()
            max_area = max(max_area, h * (n - i))
        
        return max_area
