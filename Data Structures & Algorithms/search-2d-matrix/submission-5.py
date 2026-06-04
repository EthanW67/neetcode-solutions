class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        top, bot = 0, row - 1 

        while top <= bot:
            middleRow = (top + bot) // 2

            if target > matrix[middleRow][-1]:
                top = middleRow + 1
            elif target < matrix[middleRow][0]:
                bot = middleRow - 1
            else:
                break
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        left, right = 0, col - 1

        while left <= right:
            middle = (left + right) // 2
            if target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True
        return False
            
            
