class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ # 控制边界
        if not matrix or not matrix[0]:
            return []
        res = []
        row, col = len(matrix), len(matrix[0])
        sr, r, sc, c = 0, row - 1, 0, col - 1
        while sr < r and sc < c:
            res.extend(matrix[sr][j] for j in range(sc, c))
            res.extend(matrix[i][c] for i in range(sr, r))
            res.extend(matrix[r][j] for j in range(c, sc, -1))
            res.extend(matrix[i][sc] for i in range(r, sr, -1))
            sr += 1
            r -= 1
            sc += 1
            c -= 1
        if sr == r:
            res.extend(matrix[sr][j] for j in range(sc, c+1))
        elif sc == c:
            res.extend(matrix[i][c] for i in range(sr, r+1))
        return res """
        # 边遍历边删除
        res = []
        while matrix:
            res.extend(matrix.pop(0))  # 删除矩阵第一行并添加
            if matrix and matrix[0]:
                for row in matrix:  
                    res.append(row.pop())  # 删除矩阵每一行的末尾元素并添加
            if matrix:
                res.extend(matrix.pop()[::-1])  # 删除矩阵最后一行并倒序添加
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))  # 删除矩阵每一行的第一个元素并添加
        return res
