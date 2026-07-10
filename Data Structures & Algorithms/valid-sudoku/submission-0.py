from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = defaultdict(set)
        column_seen = defaultdict(set)
        box_seen = defaultdict(set)

        for row in range(9):
            for col in range(9):
                digit = board[row][col]

                if digit == ".":
                    continue  # empty cell, nothing to check

                box_index = (row // 3) * 3 + (col // 3)

                # Check if this digit already exists in the same row, column, or box
                if digit in row_seen[row] or digit in column_seen[col] or digit in box_seen[box_index]:
                    return False

                # No duplicate found — record that we've now seen this digit here
                row_seen[row].add(digit)
                column_seen[col].add(digit)
                box_seen[box_index].add(digit)

        return True