class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = rows - 1

        while left <= right:
            current_row = (left + right) // 2
            if target > matrix[current_row][-1]:
                left = current_row + 1
            elif target < matrix[current_row][0]:
                right = current_row - 1
            else:
                break
            
        if left > right:
            return False
        
        correct_row = (left + right) // 2
        left_2 = 0
        right_2 = columns - 1

        while left_2 <= right_2:
            mid = (left_2 + right_2) // 2
            if target > matrix[correct_row][mid]:
                left_2 = mid + 1
            elif target < matrix[correct_row][mid]:
                right_2 = mid - 1
            else:
                return True
        
        return False
