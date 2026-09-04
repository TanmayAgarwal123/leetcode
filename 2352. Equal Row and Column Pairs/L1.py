from collections import Counter
import numpy as np

class Solution:#with np array
    def equalPairs(self, grid: List[List[int]]) -> int:
        matrix = np.array(grid)
        matrix_c = Counter(map(tuple, matrix))
        matrix_tc = Counter(map(tuple, matrix.T))
        val = 0
        for row in matrix_c:
            val += matrix_tc.get(row, 0) * matrix_c[row]
        return val