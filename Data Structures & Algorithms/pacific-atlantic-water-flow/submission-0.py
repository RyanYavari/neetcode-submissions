class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        '''

        Exploring all paths -> DFS

        pac, atl = set(), set()

        pac set will contain all cells that can reach the pacific
        atl will contain all cells that can reach the atlantic

        
        define dfs function

        loop through all the edges and run dfs on all the edge cells
            add to edge's ocean's set

        loop through the entire grid
            if cell is in pac and atl:
                add to output
        
        return output

        '''


        pac, atl = set(), set()

        ROWS, COLS = len(heights), len(heights[0])
        output = []


        def dfs(r, c, visit, prevHeight):
            #check base cases

            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or heights[r][c] < prevHeight):
                return
            
            visit.add((r,c))

            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        #looping through all the rows starting from left edge and right edge, doing dfs on every cell
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) #left edge -> pacific
            dfs(r, COLS-1, atl, heights[r][COLS-1]) #right edge -> atlantic
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) #top edge -> pacific
            dfs(ROWS-1, c, atl, heights[ROWS-1][c]) #bottom edge -> atlantic

        # now that both pacific and atlantic sets are populated with valid cells, we can loop 
        #through every cell in the grid and add it to output if cell is in both sets


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    output.append([r,c])
        
        return output











        