class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ref = set()

        # Check rows
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] not in ref:
                    ref.add(board[i][j])
                else:
                    return False

            ref.clear()


        # Check columns
        for j in range(9):
            ref = set()

            for i in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in ref:
                    return False

                ref.add(board[i][j])


        # Check 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                ref = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        if board[i][j] == ".":
                            continue

                        if board[i][j] in ref:
                            return False

                        ref.add(board[i][j])

        return True
        