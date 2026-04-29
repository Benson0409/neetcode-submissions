class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix == []:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])

        right = (rows * cols) - 1
        left = 0

        while left <= right:
            mid = (left + right) // 2
            
            row = mid // cols
            col = mid % cols
            mid_num = matrix[row][col]

            if target == mid_num:
                return True
            elif target < mid_num:
                right = mid - 1
            elif target > mid_num:
                left = mid + 1
        
        return False

