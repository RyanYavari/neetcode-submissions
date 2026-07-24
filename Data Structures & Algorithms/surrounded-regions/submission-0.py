class Solution:
    def solve(self, board: List[List[str]]) -> None:

        '''

        instead of capturing surrounded regions -> capture everything execept surrounded regions

        dfs -> exploring a path of connected O's

        dfs on all O's on the edge
            convert the O's to T's 

        
        after we do dfs, all the remaining O's would havew been surrounded regions -> convert to X

        convert T's to O's

        return board


        Input: board = [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","T","X","X"]
]

        '''

        visit = set()
        ROWS, COLS = len(board), len(board[0])
        
        #only want to do dfs on O's
        def dfs(r,c):
            
            #base case check
            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] != "O"):
                return
            
            visit.add((r,c))

            #explore for more O's

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            board[r][c] = "T"

            visit.remove((r,c))

        #dfs only on edges that are "O"

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
            
        #convert all surrounded O's into X's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        #convert all T's into O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        


        