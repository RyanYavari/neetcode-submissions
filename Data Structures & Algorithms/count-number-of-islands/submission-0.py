class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        '''

        start at 0, 0
        end when every cell has been visited

        loop through every cell in grid O(rows*cols):
            if cell == 1:
                increment numIslands
                perform dfs, mark cells as visited
            if cell == 0: skip
        
        return numIslands

        



        '''






        numIslands = 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):

            # if it's not a 1, dont perform dfs
            if min(r, c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == "0":
                return
            
            visit.add((r,c))

            dfs(r+1, c) #DOWN
            dfs(r-1, c) #UP
            dfs(r, c+1) #RIGHT
            dfs(r, c-1) #LEFT
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    numIslands += 1
                    dfs(r, c)
        
        return numIslands



        