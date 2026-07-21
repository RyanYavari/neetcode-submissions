class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        '''

        output: max area of an island


        maxArea = 0
        visit = set()

        ROWS, COLS = len(grid), len(grid[0])

        
        1. loop through every cell in grid
        2. identify unvisited island
            perform dfs/bfs
                count how many islands get traversed
                mark each sland as visited
            compare area with max area
        
        return maxArea

        '''

        maxArea = 0
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):

            #if out of bounds or not island, return 0
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 0:
                return 0
            
            #if island, mark as visited, increment area, and traverse
            visit.add((r,c))
            area = 1

            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c+1)
            area += dfs(r,c-1)

            return area




        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and grid[r][c] not in visit:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)
        return maxArea


        