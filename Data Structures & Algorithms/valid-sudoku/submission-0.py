class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        for y in range(n):
            row = []
            for x in range(n):
                if board[y][x] in row and board[y][x] != ".":
                    return False
                else:
                    row.append(board[y][x])
        
        for x in range(n):
            col = []
            for y in range(n):
                if board[y][x] in col and board[y][x] != ".":
                    return False
                else:
                    col.append(board[y][x])
        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                square = []
                for y in range(r, r + 3):
                    for x in range(c, c + 3):
                        if board[y][x] in square and board[y][x] != ".":
                            return False
                        else:
                            square.append(board[y][x])
        return True




            

        
        
            
            




        