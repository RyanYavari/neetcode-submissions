class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create hashmap of sets for row, col, square
            # we create a hashmap because we want to store key: value or (row/col): value
            # loop through each row and each column in O(n^2)
                # if board[r][c] == .
                    # continue
                # if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)])
                    # return False (invalid sudoku board)
            # square is row//3 and col//3 (sub boxes)
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]):       
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True
