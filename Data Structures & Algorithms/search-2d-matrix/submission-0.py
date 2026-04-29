class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right = len(matrix[0])
        left = 0

        for i in range(len(matrix)):
            if target <=  matrix[i][-1]:
                if target == matrix[i][-1]:
                    return True

                while left <= right:
                    mid = (right + left) // 2
                    if target == matrix[i][mid]:
                        return True
                    elif target < matrix[i][mid]:
                        right = mid - 1
                    elif target > matrix[i][mid]:
                        left = mid + 1
        return False

