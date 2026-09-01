class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat = []
        for i in matrix:
            mat += i
        start = 0
        end = len(mat) - 1
        
        while start <= end:
            j = start + (end - start)//2
            if mat[j] == target:
                return True
            elif mat[j] < target:
                start = j + 1
                

            elif mat[j] > target:
                end = j - 1
                
               
        return False
