class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix) -1

        rows = len(matrix)
        cols = len(matrix[0])

        # 先找列
        while top <= bottom:
            mid_row = (top + bottom) // 2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                break

        row = (top+bottom)//2
        left = 0 
        right = cols - 1

        while left <= right:
            mid = (left + right) // 2

            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1

        return False

