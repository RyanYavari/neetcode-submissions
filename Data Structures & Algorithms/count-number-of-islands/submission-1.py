class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        '''

        path exploration for each group independently -> DFS

        numIslands = 0

        search through every cell and do dfs on every cell that is an island
            increment numIslands if you find an island




        '''

        ROWS,COLS = len(grid), len(grid[0])
        visit = set()
        numIslands = 0

        def dfs(r,c):

            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] != "1"):
                return
            
            # at this point we know cell == 1

            #add to visit and search neighbors
            visit.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    numIslands += 1
                    
        
        return numIslands
                
            




        



        