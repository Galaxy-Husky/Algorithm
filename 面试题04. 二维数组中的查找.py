if not len(matrix) or not len(matrix[0]):
    return False
row, col = len(matrix), len(matrix[0])
i, j = row - 1, 0
while i >= 0 and j < col:
    n = matrix[i][j]
    if n == target:
        return True
    if n < target:
        j += 1
    if n > target:
        i -= 1
return False