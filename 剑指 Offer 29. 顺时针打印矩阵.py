class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 控制边界
        if not matrix or not matrix[0]:
            return []
        res = []
        row, col = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, col - 1, 0, row - 1
        while True:
            res.extend(matrix[top][j] for j in range(left, right + 1))
            top += 1
            if top > bottom:
                break
            res.extend(matrix[i][right] for i in range(top, bottom + 1))
            right -= 1
            if left > right:
                break
            res.extend(matrix[bottom][j] for j in range(right, left - 1, -1))
            bottom -= 1
            if top > bottom:
                break
            res.extend(matrix[i][left] for i in range(bottom, top - 1, -1))
            left += 1
            if left > right:
                break
        return res
        
        '''# 删除第一行-逆时针旋转90度
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        return res'''
