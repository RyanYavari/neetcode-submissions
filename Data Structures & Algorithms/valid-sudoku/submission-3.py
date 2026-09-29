class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        '''

        check if each row contains at least 1 digit 1-9 without duplicates -> set
        check if each column contains at least 1 digit 1-9 without duplicates -> set
        check if each of the 9 3x3 sub boxes contain digits 1-9 without duplicates -> set

        
        defaultdict(set) -> initializes any missing keys with an empty set

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        loop through rows
            loop through columns
                if board[r][c] == ".": continue

                # check rows
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3, c//3)]: # we know that this is invalid sudoku board
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r][c].add(board[r][c])
        
        return True

        '''

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                curr = board[r][c]

                if curr == ".":
                    continue

                if (curr in rows[r] or curr in cols[c] or curr in squares[(r//3, c//3)]):
                    return False
                
                rows[r].add(curr)
                cols[c].add(curr)
                squares[r//3,c//3].add(curr)
        return True
        




        