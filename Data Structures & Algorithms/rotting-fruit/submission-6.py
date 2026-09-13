class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        '''

        changing values minute by minute -> layer by layer -> BFS

        output: minimum number of minutes

        how to know when to end: when zero fresh fruit remain 

        0) get dimensions of grid, setup visit and queue
        1) loop through grid and find all rotten fruit 
            if no rotten fruits, return -1
        2) initialize variables and add rotten fruit to queue
        3) dfs 
            1. pop from queue
            2. check if fresh fruit remains, if not, return minutes
            3. check for fresh neighbors
                if fresh, add to visit
            4. if there were no fresh neighbors, return minutes
        4) return -1
        
        '''

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        minutes = 0
        fresh = 0


        # loop through and find all rotten fruit and count fresh fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2: #if its rotten
                    queue.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1


        #dfs
        while(queue) and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                # expand neighbors to find more fresh fruit
                neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr,dc in neighbors:
                    nr,nc = r+dr, c+dc

                    # check base cases.
                    if (min(nr,nc) < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit or grid[nr][nc] != 1):
                        continue
                    
                    # at this point, only fresh fruit
                    '''
                    fruit is fresh, convert to rotten, add to visit and queue
                    fresh -= 1
                    '''
                    grid[nr][nc] = 2
                    visit.add((nr,nc))
                    queue.append((nr,nc))
                    fresh -= 1
            minutes += 1
            
            # if no fresh fruits are touching rotten fruits, but fresh fruits remain, then return -1



        return minutes if fresh == 0 else -1
 





        
        


        