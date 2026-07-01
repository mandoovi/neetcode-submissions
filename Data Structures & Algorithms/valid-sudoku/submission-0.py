class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            seen = set()
            for col in range(9):
                box = board[row][col]
                if box != '.':
                    if box in seen:
                        return False
                    seen.add(box)
        
        for col in range(9):
            seen = set()
            for row in range(9):
                box = board[row][col]
                if box != '.':
                    if box in seen:
                        return False
                    seen.add(box)

        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for i in range(3):   
                    for j in range(3):   
                        box = board[row + i][col + j]
                        if box != '.':
                            if box in seen:
                                return False
                            seen.add(box)

        return True



        