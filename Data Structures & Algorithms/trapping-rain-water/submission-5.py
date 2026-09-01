class Solution:
    def trap(self, height: List[int]) -> int:

        p1=0
        p2=1
        area = 0
        current_area = 0

        while p2 < len(height) and p1 < len(height):
            if height[p2] < height[p1]:
                current_area += height[p1] - height[p2]
                p2 += 1
                if p2 >= len(height):
                    # Fix: If p2 reaches the end without finding a bar >= height[p1],
                    # re-calculate from the right to catch remaining water.
                    height = height[p1:][::-1]
                    return area + self.trap(height)

                
            elif height[p2] >= height[p1]:
                area += current_area
                current_area = 0
                p1 = p2
                p2 += 1
        return area
        