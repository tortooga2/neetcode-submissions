class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        max_height = sorted(heights)[-1]
        max_area = 0
        for i in range(1, max_height + 1):
            count = 0
            for h in heights:
                if h >= i:
                    count += 1
                else:
                    if max_area < i * count:
                        max_area = i * count
                    count = 0

                
            if max_area < i * count:
                max_area = i * count

        
        return max_area
                
                


        

        
        
                



        