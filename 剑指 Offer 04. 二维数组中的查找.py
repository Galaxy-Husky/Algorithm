class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. Z字形查找 左下角or右上角 O(m+n) O(1)
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            n = matrix[i][j]
            if n == target:
                return True
            if n < target:
                j += 1
            if n > target:
                i -= 1
        return False