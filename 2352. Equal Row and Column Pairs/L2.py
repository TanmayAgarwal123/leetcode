class Solution:#without np array
    def equalPairs(self, grid: List[List[int]]) -> int:
        matrix_c = Counter(map(tuple, grid))
        matrix_tc = Counter(tuple(row) for row in zip(*grid))# Another approach - matrix_tc = Counter(zip(*grid))
        val = 0
        for row in matrix_c:
            val += matrix_tc.get(row, 0) * matrix_c[row]
        return val