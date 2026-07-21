class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

    
        # initialzie variables
        visit = set()
        n = len(grid)
        queue = deque()
        neighbors = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1, -1], [-1, 1], [1, 1]]

        # check if clear path exists
        if grid[0][0] == 1:
            return -1
        
        # clear path exists, initialize first cell
        visit.add((0,0))
        queue.append((0,0))

        #bfs
        length = 1 # length starts as one since length of a clear path is the number of visited cells of the path
        while(queue):
            for i in range(len(queue)):

                # deque the leftmost variables
                r, c = queue.popleft()

                # check if we are at the target cell. if so, return shortest path
                if r == n-1 and c == n-1:
                    return length
                
                # not at target yet. expand to neighbors
                for dr, dc in neighbors:
                    nr, nc = r+dr, c+dc
                    # check for base cases (4)
                        #1. below 0
                        #2. above length of matric
                        #3. visited already?
                        #4. blocked? cell == 1
                    if (min(nr, nc) < 0 or nr == n or nc == n or (nr,nc) in visit or grid[nr][nc] == 1):
                        continue
                    
                    # if valid cell, add to queue and visit
                    visit.add((nr,nc))
                    queue.append((nr,nc))
            # increment length
            length += 1
        
        return -1




        