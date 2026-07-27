class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        lp = 0
        rp = (rows * cols) - 1

        while lp <= rp:
            mid_index = (lp + rp) // 2

            row = mid_index // cols
            col = mid_index % cols
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                lp = mid_index + 1
            else:
                rp = mid_index - 1

        return False