from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = defaultdict(set)
        col_seen = defaultdict(set)
        box_seen = defaultdict(set)

        for row in range(9):
            for col in range(9):
                digit = board[row][col]

                if digit == ".":
                    continue

                box_index = (row // 3) * 3 + (col // 3)
                
                if digit in row_seen[row] or digit in col_seen[col] or digit in box_seen[box_index]:
                    return False

                row_seen[row].add(digit)
                col_seen[col].add(digit)
                box_seen[box_index].add(digit)

        return True